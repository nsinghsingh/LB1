import pandas as pandas
import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import matplotlib
matplotlib.use('Agg')

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
print(us_census.head())

#8
plt.scatter(us_census['Women'], us_census['Income']) #Soll nicht funktionieren nach Aufgabe
plt.show()
plt.savefig('myhistogram.png')

#9
us_census = us_census.fillna(value={"Women":us_census['TotalPop'] - us_census['Men']})
print(us_census.head())

#10
duplicates = us_census.duplicated(subset='TotalPop')
print(duplicates)

#11
us_census = us_census.drop_duplicates(subset='TotalPop')
print(us_census)

#12
plt.scatter(us_census['Women'], us_census['Income']) #Soll funktionieren nach Aufgabe
plt.show()
plt.savefig('myhistogram.png')

#13
print(us_census.columns)

#14
races = ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']

for race in races:
  us_census[race] = us_census[race].replace('%', '', regex=True)
  us_census[race] = pandas.to_numeric(us_census[race])
  us_census = us_census.fillna(value={race:0})
  plt.hist(us_census[race]) #Soll funktionieren nach Aufgabe
  plt.show()
  plt.savefig(race + '_histogramm.png')
print(us_census.dtypes)
print(us_census.head())

#15
