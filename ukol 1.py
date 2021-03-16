import pandas
jobs = pandas.read_csv('DataAnalyst.csv')
print(jobs.columns)
print(jobs.head)
print(jobs.shape)
print(jobs.iloc[9]) #jeden radek, : se dava jen kdyz chceme vybrany rozsah
#Podívej se, kde budou pracovat zájemci vybraní na dvanáctou až dvacátou pozici.
print(jobs.iloc[12:30,[1,6]])