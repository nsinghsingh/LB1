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
genders = us_census.GenderPop.str.split('_', expand=True)


#7
genders = genders.replace('(F|M)', '', regex=True)
genders[0] = pandas.to_numeric(genders[0])
genders[1] = pandas.to_numeric(genders[1])
