# Dependency needed to install file

# If running the notebook on your machine, else leave it comented
#!pip install xlrd

#!pip install openpyxl 
import piplite
await piplite.install(['xlrd','openpyxl'])

# Import required library

import pandas as pd

# Read data from CSV file

# csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
# df = pd.read_csv(csv_path)

from pyodide.http import pyfetch
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


await download(filename, "TopSellingAlbums.csv")
df = pd.read_csv("TopSellingAlbums.csv")

#filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"
#df = pd.read_csv(filename)

# First five rows of the dataframe

df.head()

# Read data from Excel file and print the first five rows

xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'

await download(xlsx_path, "TopSellingAlbums.xlsx")
df = pd.read_excel("TopSellingAlbums.xlsx")
df.head()

# Access to the column Lenght

x = df[['Length']]
x

# Get the column as a dataframe

x = df[['Artist']]
type(x)

# Access to multiple columns

y = df[['Artist','Length','Genre']]
y

# Access the value on thre first row and the first column

df.iloc[0,0]
