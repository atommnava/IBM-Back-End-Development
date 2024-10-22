# Pandas is an API

import pandas as pd
import matplotlib.pyplot as plt

dict_={'a':[11,21,32], 'b':[12,22,23]}

# When you create a Pandas object with the dataframe constructor, in API lingo this is an "instance". 
# The data in the dictionary is passed along to the pandas API. 
# You then use the dataframe to communicate with the API.
df = pd.DataFrame(dict_)
type(df)

# When you call the method `head` the dataframe communicates with the API displaying the first few rows of the dataframe.
df.head()
df.mean()

# REST APIs

# Rest APIs function by sending a request, the request is communicated via HTTP message. 
# The HTTP message usually contains a JSON file. This contains instructions for what operation we would like the service or resource to perform. 
# In a similar manner, API returns a response, via an HTTP message, this response is usually contained within a JSON.

!pip install nba_api
from nba_api.stats.static import teams
import matplotlib.pyplot as plt

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

# The method get_teams() returns a list of dictionaries.

nba_teams = teams.get_teams()
nba_teams[0:3]

dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
df_teams.head()

# Will use the team's nickname to find the unique id, we can see the row that contains the warriors by using the column nickname as follows:
df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors

# We can use the following line of code to access the first column of the DataFrame
id_warriors=df_warriors[['id']].values[0][0]
# we now have an integer that can be used to request the Warriors information 
id_warriors

# The function "League Game Finder " will make an API call, it's in the module
from nba_api.stats.endpoints import leaguegamefinder


