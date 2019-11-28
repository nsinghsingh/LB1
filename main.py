import pandas as pandas
import numpy as numpy
import matplotlib
import seaborn as sns
import glob

#2
states_files = glob.glob("states*.csv")
df_list = []

for state in states_files:
  new_df = pandas.read_csv(state)
  df_list.append(new_df)
  
us_census = pandas.concat(df_list)

#3
print(us_census.dtypes)
print(us_census.columns)

#4
print(us_census.head())

#5
us_census['Income'] = us_census['Income'].replace('\$', '', regex=True)
print(us_census.head())

#6
us_census[['Men', 'Women']] = us_census.GenderPop.str.split('_', expand=True)

#7
us_census[['Men', 'Women']] = us_census[['Men', 'Women']].replace('(F|M)', '', regex=True)
us_census['Women'] = pandas.to_numeric(us_census['Women'])
us_census['Men'] = pandas.to_numeric(us_census['Men'])

#8
