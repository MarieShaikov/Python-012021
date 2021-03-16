import pandas
staty = pandas.read_json('staty.json')
#print(countries.head)
staty = staty.set_index("name")
# print(staty.index)
# print(staty.loc["Czech Republic"]) #gives me all info about this country
# print(staty.loc["Czech Republic":"Dominican Republic"])
# print(staty.loc[["Czech Republic", "Slovakia"], "capital"])
# print(staty.loc[["Poland", "Slovakia", "Austria", "Germany"], ["capital", "gini", "population"]])
#
# print(staty[["population", "area"]]) #if more than one variable, use double brackets [[ ]]
#

populace = staty["population"] #prevod do typu serie
print(populace.sum())

pidistaty = (staty[staty["population"] < 1000]) #return only countries will less than 1000 population
print(pidistaty[["area", "population"]]) #chybejicic data u rozhlohy - tohle by se melo filtrovat, cleaning data is important
