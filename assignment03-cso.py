# Output historical exchequer account data from cso to file.
# Author Finbar Dennehy

# Import required packages
import requests
import json

# Get data from cso
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"
response = requests.get(url)
historic_exchequer_account = response.json()

# Set file name
file_name = 'cso.json'

# Write data to file
with open(file_name, 'w') as fp:
    json.dump(historic_exchequer_account, fp, indent=4)

# Print message at end of script
print(f"Exchequer data has been written to {file_name}")