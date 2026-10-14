# Libraries for retrieving data from the web and handling zip files
import requests, zipfile
from io import StringIO
import io
import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

# Specify the url with data
url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'

# Acquire data from the url
r = requests.get(url, stream=True)

# read and extract the zipfile
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

anime_data = pd.read_csv('MyAnimeList-Database-master/data/anime.csv')
anime_list = pd.read_csv('MyAnimeList-Database-master/data/animelist.csv')
anime_synop = pd.read_csv('MyAnimeList-Database-master/data/anime_with_synopsis.csv')

print(anime_data.head())

# Check information on all columns
anime_data.info()

# Check basic statistics
print(anime_data.describe())

#?----------DataFrame Basics------------------

# Specify column name (if one)
print(anime_data['Score'])

# It can also be written like this
print(anime_data.Score)
# Specify column names (if multiple)
print(anime_data[['Name', 'Score']])

cols_to_use = [
    'MAL_ID', 'Name', 'Score', 'Genres', 'Type', 'Aired', 'Studios', 'Source','Members'
]
anime_data_extracted = anime_data[cols_to_use]
print(anime_data_extracted.head())

#?----Extracting Only Specific Rows --------

# Specify row name
print(anime_data_extracted[0:3])

df = pd.DataFrame({
    'ID': [100, 101, 102, 103],
    'City': ['Tokyo', 'Osaka', 'Kyoto', 'Nagoya'],
    'Birth_year': [1990, 1989, 1992, 1995],
    'Name': ['Hiroshi', 'Akiko', 'Yuki', 'Satoru']
}, index=['a', 'b', 'c', 'd'])



print(df['a':'c'])
# Specify row name (if one)
print(anime_data_extracted.loc[4])

# Specify row names (if multiple)
print(anime_data_extracted.loc[3:8])

# Specify column name (if one)
print(anime_data_extracted.loc[:, 'Name'])
# Specify column names (if multiple)
print(anime_data_extracted.loc[:, ['MAL_ID', 'Name']])
# Specify 3 rows from 0 and columns 'MAL_ID' and 'Name'
print(anime_data_extracted.loc[0:3, ['MAL_ID', 'Name']])
# Specify first 4 rows and 1st and 3rd columns
print(anime_data.iloc[0:4, [0, 2]])
# Get 'ID' of line 0
print(anime_data.at[0, 'Name'])
# Creating new column
df['Score'] = np.arange(4) * 10
print(df)
df.at[0, 'Birth_year'] = 2000
print(df)

#? -------- Extracting Data whit Specific Conditions -----------
print(anime_data_extracted['Score'] != 'Unknown')
#　Condition filtering
anime_data_extracted = anime_data_extracted[anime_data_extracted['Score'] != 'Unknown']
print(anime_data_extracted.head())
# 'Studios' is Nomad or Sunrise
print(anime_data_extracted[(anime_data_extracted['Studios'] == 'Nomad') | (anime_data_extracted['Studios'] == 'Sunrise')].head())

#　'Studios' is either 'Sunrise' or 'Nomad'
print(anime_data_extracted[anime_data_extracted['Studios'].isin(['Sunrise', 'Nomad'])].head())

#? ------ examples of nan and null
print(anime_data_extracted.isnull())

# Determine null and sum up
print(anime_data_extracted.isnull().sum())