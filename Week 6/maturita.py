import pandas
u202 = pandas.read_csv('u202.csv')
print(u202[u202["znamka"].isnull()]) # student nema znamku u techto predmetu, 0 jako chybejici data






