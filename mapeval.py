'''
Script to evaluate the performance of a matching algorithm.
Metrics:
- Correct mapping is in the top n returned candidate(s)
- Auto-match is correct

1. Config
    Set the performance metrics (i.e. top n) and auto-match rules
    3. Configure field names
    4. Set Target source
2. Load spreadsheet
3. Auto-match (retrieve n candidates)
4. Evaluate metrics results
5. Report results
'''
import argparse
import time
import json
import requests
import pandas as pd

start_time = time.time()

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--token', required=True)
parser.add_argument('-f', '--file', required=False, default="/Users/sny/workspace/ocl/mapeval/NMRS ciel maps only.xlsx")
parser.add_argument('-r', '--repo', required=False, default="/orgs/CIEL/sources/CIEL/v2024-10-04/")
parser.add_argument('-e', '--env', default="http://localhost:8000")
parser.add_argument('-s', '--semantic', default='false', choices=['true', 'false'])
parser.add_argument('-c', '--chunk', default=200)
parser.add_argument('-nr', '--results', default=3)
parser.add_argument('-v', '--verbose', default="0")
args = parser.parse_args()

# IMPORT FILE SETTINGS: KenyaEMR Concepts Mapped Dataset.xlsx
# import_filename = "/Users/jonathanpayne/Google Drive/My Drive/OCL/OCL Shared/Mapping Tool/Sample Input Data/KenyaEMR Concepts Mapped Dataset.xlsx"
# import_file_type = 'xlsx'  # e.g. csv, xlsx
# correct_map_column_name = "True CIEL Concept"  # Example: to_concept_code
# map_column_to_algorithm_key = {"Variable Name": "name", "Datatype": "datatype"}

# IMPORT FILE SETTINGS: NMRS ciel maps only.xlsx
import_filename = args.file
import_file_type = args.file.split('.')[-1]  # e.g. csv, xlsx
map_column_to_algorithm_key = {
    "from_concept_name_resolved": "name",
}
correct_map_column_name = "to_concept_code"  # Example: to_concept_code

# IMPORT FILE SETTINGS: Small Nigeria sample
# import_filename = "/Users/jonathanpayne/Google Drive/My Drive/OCL/OCL Shared/Mapping Tool/Sample Input Data/NMRS mapping issues questions 2024-04-30.xlsx"
# import_file_type = 'xlsx'  # e.g. csv, xlsx
# correct_map_column_name = "CIEL Code"  # Example: to_concept_code
# map_column_to_algorithm_key = {"id": "local-id", "local concept name": "name"}


# ADDITIONAL SETTINGS
semantic = args.semantic
top_n_threshold = args.results  # e.g. Top 1, or Top 3
target_repo_url = args.repo
ocl_api_token = args.token
ocl_api_match_url = args.env + "/concepts/$match/"
max_chunk_size = int(args.chunk)
chunk_delay = 0  # in seconds

# CONSTANTS
list_algorithm_keys = ["id", "name", "synonyms", "description", "concept_class", "datatype", "same_as_map_codes", "other_map_codes"]
candidates_limit = max(top_n_threshold, 1)  # Get at least 1 candidate. For auto-matching, will need to get at least 2.
params = {
    "includeSearchMeta": True,
    "semantic": semantic,
    "limit": candidates_limit,
    "bestMatch": True
}
headers = {"Authorization": "Token %s" % (ocl_api_token)}

# IMPORT
if import_file_type == 'csv':
    df = pd.read_csv(import_filename)
elif import_file_type == 'xlsx':
    df = pd.read_excel(import_filename)
else:
    print("unknown file type", import_file_type)
    exit()

# Change column names, convert to dictionary and chunk
df.rename(columns=map_column_to_algorithm_key, inplace=True)
data = json.loads(df.to_json(orient="records"))  # serialize/deserialize to get rid of funky datatypes
list_of_chunked_data = [data[i * max_chunk_size:(i + 1) * max_chunk_size] for i in range((len(data) + max_chunk_size - 1) // max_chunk_size)]

# Match and evaluate one chunk at a time
num_correct_matches_in_top_n = 0
num_excluded = 0
num_new_concept_proposed = 0
chunk_num = 0
unmatched = []
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
    print("\n", chunk_num, 'chunk len:', len(new_chunk))
    payload = {
        "rows": new_chunk,
        "target_repo_url": target_repo_url
    }
    if chunk_num > 1:
        time.sleep(chunk_delay)
    r = requests.post(ocl_api_match_url, json=payload, params=params, headers=headers)
    response = r.json()
    # Evaluate the results: top-N, auto-match
    for match_set in response:
        if not match_set["row"][correct_map_column_name]:
            num_excluded += 1
        elif str(match_set["row"][correct_map_column_name]).lower() == "new":
            num_new_concept_proposed += 1
        else:
            matched_candidate = next((candidate for candidate in match_set["results"] if str(int(match_set["row"][correct_map_column_name])) == str(int(candidate["id"]))), None)
            if matched_candidate:
                print(str(matched_candidate["id"]), " ", sep="", end="")
                num_correct_matches_in_top_n += 1
                chunk_match_count += 1
            else:
                unmatched.append(match_set['row'])

    print("\nChunk Match Count: ", f"{chunk_match_count} ({round((chunk_match_count/max_chunk_size) * 100, 2)}%)")

print("\nRESULTS:")
print("  Semantic: ", semantic)
print("  top_n_threshold: ", top_n_threshold)
print("  num_correct_matches_in_top_n: ", num_correct_matches_in_top_n)
print("  num_excluded_rows: ", num_excluded)
print("  num_new_concept_proposed: ", num_new_concept_proposed)
print("  total_rows:", len(df))
print("  match_perc: ", round((num_correct_matches_in_top_n/len(df)) * 100, 2))
print("  Elapsed Seconds:", time.time() - start_time)
if args.verbose in ['true', '1']:
    print("\n\nUnmatched", len(unmatched))
    from pprint import pprint
    pprint(unmatched)
