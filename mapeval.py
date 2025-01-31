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
import time
import json
import requests
import pandas as pd


# IMPORT FILE SETTINGS: NMRS Concept Request from CCFN 22012025 final mappings.xlsx
import_filename = "/Users/jonathanpayne/Google Drive/My Drive/OCL/OCL Shared/Mapping Tool/Sample Input Data/NMRS Concept Request from CCFN 22012025 final mappings.xlsx"
import_file_type = 'xlsx'  # e.g. csv, xlsx
correct_map_column_name = "CIEL concept id"  # Example: to_concept_code
map_column_to_algorithm_key = {"ELEMENTS - clean": "name"}

# IMPORT FILE SETTINGS: KenyaEMR Concepts Mapped Dataset.xlsx
# import_filename = "/Users/jonathanpayne/Google Drive/My Drive/OCL/OCL Shared/Mapping Tool/Sample Input Data/KenyaEMR Concepts Mapped Dataset.xlsx"
# import_file_type = 'xlsx'  # e.g. csv, xlsx
# correct_map_column_name = "True CIEL Concept"  # Example: to_concept_code
# map_column_to_algorithm_key = {"Variable Name": "name", "Datatype": "datatype"}

# IMPORT FILE SETTINGS: NMRS ciel maps only.xlsx
# import_filename = "/Users/jonathanpayne/Google Drive/My Drive/OCL/OCL Shared/Mapping Tool/Sample Input Data/NMRS ciel maps only.xlsx"
# import_file_type = 'xlsx'  # e.g. csv, xlsx
# correct_map_column_name = "to_concept_code"  # Example: to_concept_code
# map_column_to_algorithm_key = {"from_concept_name_resolved": "name"}

# IMPORT FILE SETTINGS: Small Nigeria sample
# import_filename = "/Users/jonathanpayne/Google Drive/My Drive/OCL/OCL Shared/Mapping Tool/Sample Input Data/NMRS mapping issues questions 2024-04-30.xlsx"
# import_file_type = 'xlsx'  # e.g. csv, xlsx
# correct_map_column_name = "CIEL Code"  # Example: to_concept_code
# map_column_to_algorithm_key = {"id": "local-id", "local concept name": "name"}


# ADDITIONAL SETTINGS
top_n_threshold = 1  # e.g. Top 1, or Top 3
target_repo_url = "/orgs/CIEL/sources/CIEL/v2023-09-11/"
ocl_api_token = ''
ocl_api_match_url = "https://api.qa.openconceptlab.org/concepts/$match/"
max_chunk_size = 500
chunk_delay = 0  # in seconds

# CONSTANTS
list_algorithm_keys = ["id", "name", "synonyms", "description", "concept_class", "datatype", "same_as_map_codes", "other_map_codes"]
candidates_limit = max(top_n_threshold, 1)  # Get at least 1 candidate. For auto-matching, will need to get at least 2.
params = {
    "includeSearchMeta": True,
    "semantic": False,
    "bestMatch": True,
    "limit": candidates_limit
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
for chunk in list_of_chunked_data:
    # Request match results
    chunk_num += 1
    print("\n", chunk_num, 'chunk len:', len(chunk))
    payload = {
        "rows": chunk,
        "target_repo_url": target_repo_url
    }
    if chunk_num > 1:
        time.sleep(chunk_delay)
    r = requests.post(ocl_api_match_url, json=payload, params=params, headers=headers)
    response = r.json()

    # Evaluate the results: top-N, auto-match
    for match_set in response:
        # correct_map_value = match_set["row"][correct_map_column_name]
        if not match_set["row"][correct_map_column_name]:
            num_excluded += 1
        elif str(match_set["row"][correct_map_column_name]).lower() == "new":
            num_new_concept_proposed += 1
        else:
            candidate_num = 0
            for candidate in match_set["results"]:
                candidate_num += 1
                try:
                    if candidate_num <= top_n_threshold and str(int(match_set["row"][correct_map_column_name])) == str(int(candidate["id"])):
                        print(str(candidate["id"]), " ", sep="", end="")
                        num_correct_matches_in_top_n += 1
                        break
                except:
                    d = 0

print("\nRESULTS:")
print("  top_n_threshold: ", top_n_threshold)
print("  num_correct_matches_in_top_n: ", num_correct_matches_in_top_n)
print("  num_excluded_rows: ", num_excluded)
print("  num_new_concept_proposed: ", num_new_concept_proposed)
print("  total_rows:", len(df))
