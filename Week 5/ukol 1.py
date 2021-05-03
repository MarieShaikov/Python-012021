import pandas
jobs = pandas.read_csv('DataAnalyst.csv')
print(jobs.columns)
print(jobs.head)
print(jobs.shape)
print(jobs.iloc[9]) #jeden radek, : se dava jen kdyz chceme vybrany rozsah

#Podívej se, kde budou pracovat zájemci vybraní na dvanáctou až dvacátou pozici.
print(jobs.iloc[12:21,[1,6]]) #iloc is number, range between rows or columns