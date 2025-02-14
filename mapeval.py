'''
Script to evaluate the performance of a matching algorithm.
Current metrics: top-n, elapsed time
Planned: auto-match is correct
'''
import argparse
import time
import json
import requests
import pandas as pd


def mapeval(api_token="", api_match_url="", input_filename="", target_repo="", correct_map_column_name="",
            column_map={}, semantic=False, max_chunk_size=200, knn_num_candidates=1000, top_n_threshold=5,
            verbosity=0, output_filename=""):
    start_time = time.time()

    # CONSTANTS
    list_algorithm_keys = ["id", "name", "synonyms", "description", "concept_class", "datatype",
                           "same_as_map_codes", "other_map_codes"]
    params = {
        "includeSearchMeta": True,
        "semantic": semantic,
        "limit": top_n_threshold,
        "kNearest": 5,
        "numCandidates": knn_num_candidates,
        "bestMatch": False
    }
    headers = {}
    if api_token:
        headers["Authorization"] = "Token %s" % (api_token)

    # Print script configuration
    if verbosity:
        print("\nCONFIGURATION:")
        print("  Matching API endpoint: ", api_match_url)
        if api_token:
            print("  API token: *******")
        print("  Input Filename: ", input_filename)
        print("  Output Filename: ", output_filename)
        print("  Target Repository: ", target_repo)
        print("  Correct Map Concept ID Column Name: ", correct_map_column_name)
        print("  Semantic Search: ", semantic)
        print("  Top-n Threshold: ", top_n_threshold)
        print("  Max Chunk Size: ", max_chunk_size)
        print("  Number of Candidates: ", knn_num_candidates)
        print("  Verbosity: ", verbosity)
        if column_map:
            print("  Column Mapping: ", json.dumps(column_map, indent=4))

    # Load input file
    import_file_type = input_filename.split('.')[-1]  # e.g. csv, xlsx
    if import_file_type == 'csv':
        df = pd.read_csv(input_filename)
    elif import_file_type == 'xlsx':
        df = pd.read_excel(input_filename)
    else:
        print("unknown file type", import_file_type)
        exit()

    # Process import file: Change column names, convert to dictionary and chunk
    df.rename(columns=column_map, inplace=True)
    data = json.loads(df.to_json(orient="records"))  # serialize/deserialize to get rid of funky datatypes
    list_of_chunked_data = [data[i * max_chunk_size:(i + 1) * max_chunk_size] for i in range((len(data) + max_chunk_size - 1) // max_chunk_size)]
    if verbosity:
        print("\nINPUT FILE:")
        print("  Total Rows: ", len(df))
        print("  # Chunks: ", len(list_of_chunked_data))

    # Match and evaluate one chunk at a time
    num_correct_matches_in_top_n = [0] * top_n_threshold
    num_auto_match = 0 # 'search_meta.match_type=very_high'
    num_excluded = 0
    num_new_concept_proposed = 0
    chunk_num = 0
    unmatched = []
    row_num = 0
    row_results = []
    print("\nMATCHING:")
    for chunk in list_of_chunked_data:
        chunk_match_count = 0
        new_chunk = []
        for row in chunk:
            row['name'] = row.get('name', None) or ""
            row['synonyms'] = [row['name']]
            row.pop('id', None)
            new_chunk.append(row)

        # Request match results
        chunk_num += 1
        payload = {
            "rows": new_chunk,
            "target_repo_url": target_repo
        }
        if verbosity:
            print("\n  Chunk #: ", chunk_num, ' Chunk len:', len(new_chunk), api_match_url, json.dumps(params))
        r = requests.post(api_match_url, json=payload, params=params, headers=headers)
        response = r.json()

        # Evaluate the results one row_matches at a time
        for row_matches in response:
            row_num += 1

            # Sort row_matches["results"] by search_meta["search_score"]
            row_matches["results"] = sorted(row_matches["results"], key=lambda candidate: candidate["search_meta"]["search_score"], reverse=True)

            # Evaluate top-n metric
            if correct_map_column_name:
                if not row_matches["row"][correct_map_column_name]:
                    num_excluded += 1
                elif str(row_matches["row"][correct_map_column_name]).lower() == "new":
                    num_new_concept_proposed += 1
                else:
                    matched_candidate_index = next((index for index, candidate in enumerate(row_matches["results"]) if str(row_matches["row"][correct_map_column_name]) == str(candidate["id"])), None)
                    if matched_candidate_index is not None:
                        matched_candidate = row_matches["results"][matched_candidate_index]
                        if verbosity >= 2:
                            print(str(matched_candidate["id"]), " ", sep="", end="")
                        if matched_candidate['search_meta']['match_type'] == 'very_high':
                            num_auto_match += 1
                        for i in range(matched_candidate_index, top_n_threshold):
                            num_correct_matches_in_top_n[i] += 1
                        chunk_match_count += 1
                    else:
                        unmatched.append(row_matches['row'])

            # Sort candidate by search_meta["search_score"] - remove after this is applied in the API
            candidate_scores = [candidate["search_meta"]["search_score"] for candidate in row_matches["results"]]

            # Store candidate scores for analytics
            row_results.append(candidate_scores.copy())

        print("  Chunk Match Count: ", f"{chunk_match_count} ({round((chunk_match_count/len(new_chunk)) * 100, 2)}%)")

    # Results
    elapsed_seconds = time.time() - start_time
    results = {
        "total_rows": len(df),
        "num_auto_matches": num_auto_match,
        "num_correct_matches_in_top_n": num_correct_matches_in_top_n,
        "num_excluded_rows": num_excluded,
        "num_new_concept_proposed": num_new_concept_proposed,
        "elapsed_seconds": elapsed_seconds,
        "row_candidate_scores": row_results
    }

    # Report results
    if verbosity:
        print("\nRESULTS:")
        print("  total_rows:", len(df))
        print("  num_auto_matches: ", num_auto_match)
        print("  num_correct_matches_in_top_n: ", end="")
        for i, value in enumerate(num_correct_matches_in_top_n, start=1):
            print(f"{i}:{value}", end=" ")
        print("\n  num_excluded_rows: ", num_excluded)
        print("  num_new_concept_proposed: ", num_new_concept_proposed)
        print("  num_to_match: ", len(df) - num_new_concept_proposed - num_excluded)
        print("  Elapsed Seconds:", elapsed_seconds)

    # Print unmatched rows
    if verbosity >= 2:
        print("\n\nUnmatched:", len(unmatched))
        from pprint import pprint
        pprint(unmatched)

    return results


# CLI
parser = argparse.ArgumentParser(prog='mapeval.py', description='Evaluate the performance of a matching algorithm')
parser.add_argument('-t', '--token', required=True, help="OCL API token")
parser.add_argument('-i', '--inputfile', required=True, help="File of input data to be mapped")
parser.add_argument('-r', '--repo', required=False, help="Map target repo, e.g. /orgs/CIEL/sources/CIEL/v2024-10-04/", default="/orgs/CIEL/sources/CIEL/v2024-10-04/")
parser.add_argument('-e', '--env', default="http://localhost:8000", help="OCL API environment, e.g. https://api.qa.openconceptlab.org")
parser.add_argument('--endpoint', default="/concepts/$match/", help="$match endpoint, e.g. /concepts/$match/")
parser.add_argument('--correctmap', default="correct_map_concept_id", help="Column name of the correct map")
parser.add_argument('--columnmap_filename', help="JSON file containing column mappings")
parser.add_argument('-s', '--semantic', default='false', choices=['true', 'false'])
parser.add_argument('-c', '--chunk', default=200, help="Max chunk size to send to $match algorithm at a time")
parser.add_argument('--numcandidates', default=5000, help="Approximate number of nearest neighbor candidates to consider on each shard")
parser.add_argument('-n', '--topn', default=5, help="Number of results to consider for top-n test")
parser.add_argument('-v', '--verbosity', default="0")
parser.add_argument('-o', '--output', help="Analytics output file to write the results")
args = parser.parse_args()

# Convert columnmap_filename argument to dictionary, if provided
column_map = {}
if args.columnmap_filename:
    with open(args.columnmap_filename, 'r') as f:
        column_map = json.load(f)

# Call the mapeval method with parsed arguments
api_match_url = args.env + args.endpoint
run_results = mapeval(
    api_token=args.token,
    api_match_url=api_match_url,
    input_filename=args.inputfile,
    target_repo=args.repo,
    correct_map_column_name=args.correctmap,
    column_map=column_map,
    semantic=args.semantic in ['true', '1'],
    max_chunk_size=int(args.chunk),
    knn_num_candidates=int(args.numcandidates),
    top_n_threshold=int(args.topn),
    verbosity=int(args.verbosity)
)

# Write analytics output file
output_filename = args.output
if output_filename:
    with open(output_filename, 'w') as f:
        f.write(json.dumps(run_results, indent=4))
