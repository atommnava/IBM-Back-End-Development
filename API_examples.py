# API Examples

# Example 1: RandomUser API
!pip install randomuser
!pip install pandas

from randomuser import RandomUser
import pandas as pd

# First, we will create a random user object, r.
r = RandomUser()

# Then, using generate_users() function, we get a list of random 10 users
some_list = r.generate_users(10)
some_list

# The "Get Methods" functions mentioned at the beginning of this notebook, can generate the required parameters to construct a dataset. 
# For example, to get full name, we call get_full_name() function

name = r.get_full_name()

# Let's say we only need 10 users with full names and their email addresses. 
# We can write a "for-loop" to print these 10 users

for user in some_list:
    print(user.get_full_name(), " ", user.get_email())

for user in some_list:
    print(user.get_picture())

get_users()
df1 = pd.DataFrame(get_users())

# Example 2: Fruityvice API

import requests
import json
import pandas as pd

# We will obtain the fruityvice API data using requests.get("url") function. The data is in a json format
data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

results = json.loads(data.text)

# We will convert our json data into pandas data frame.
pd.DataFrame(results)

df2 = pd.json_normalize(results)
df2

cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']), (cherry.iloc[0]['genus'])



