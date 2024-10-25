# Working with different file formats

# Reading data from CSV in Python

# We use pandas.read_csv() function to read the csv file. 
# In the parentheses, we put the file path along with a quotation mark as an argument, so that pandas will read the file into a data frame from that address. 
# The file path can be either a URL or your local file address.
import piplite
await piplite.install(['seaborn', 'lxml', 'openpyxl'])

import pandas as pd

from pyodide.http import pyfetch

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "addresses.csv")

df = pd.read_csv("addresses.csv", header=None)
df

# Adding column name to the DataFrame
# We can add columns to an existing DataFrame using its columns attribute

df.columns = ['First Name', 'Last Name', 'Location', 'City', 'State', 'Area Code']
df

# Selecting a single column
df["First Name"]

# ----------------JSON file Format ---------------------

# Python supports JSON through a built-in package called json. To use this feature, we import the json package in Python script

import json

# Writing JSON to a File

import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address' : {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# Serialization using dump() function

with open('person.json', 'w') as f: # Writing JSON object
    json.dump(person, f)

# Serialising json
json_object = json.dumps(person, indent = 4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print(json_object)
