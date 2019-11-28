import pandas as pandas
import numpy as numpy
import matplotlib
import seaborn as sns
import glob

states_files = glob.glob("states*.csv")
df_list = []

for state in states_files:
  new_df = pandas.read_csv(state)
  df_list.append(new_df)
  
us_census = pandas.concat(df_list)


