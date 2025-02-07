# oclmap
OCL Mapper user interface

### Run Dev
1. `docker-compose up -d`
2. Visit http://localhost:4004

### Run Dev with KeyCloak (SSO)
1. `docker-compose -f docker-compose.yml -f docker-compose.sso.yml up -d`
2. Visit http://localhost:4004

### Run Production (do check CORS origin policy with API_URL)
1. `docker-compose -f docker-compose.yml up -d`
2. Visit http://localhost:4004


### Eslint
```
docker exec -it <container_name> bash -c "eslint src/ --ext=.js*"
```

#### Major/minor version increase

In order to increase major/minor version you need to set the new version in [package.json](package.json).

### Evaluating Matching Algorithms with `mapeval.py`
`mapeval.py` is a simple CLI script (command-line interface) to evaluate the performance (e.g. matching accuracy, time, etc.) of a matching algorithm.
You must provide at least a file of the input data to be matched (`-f` or `--file`). The evaluation requires that the input spreadsheet has a column
with the ultimate mapping decision made. It can have one of three types of values:
* Concept ID, e.g. `1459` or `A10.1`
* "New" - if a new concept was proposed
* Empty - if the row was excluded (not mapped to a concept)

See all command line arguments like this:
```
python3 mapeval.py --help
```

Example:
```
python3 mapeval.py -t=[your-api-token] -r=/orgs/CIEL/sources/CIEL/v2023-09-11/ -e=https://api.qa.openconceptlab.org -f=./samples/NMRS\ Concept\ Request\ from\ CCFN\ 22012025\ final\ mappings.xlsx --correct=Correct\ Map\ CIEL\ Concept\ ID
```
