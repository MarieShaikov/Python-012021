import pandas
staty = pandas.read_json('../Week 7/staty.json')
#print(countries.head)
staty = staty.set_index("name")
print(staty.index)
print(staty.loc["Czech Republic"]) #gives me all info about this country
print(staty.loc["Czech Republic":"Dominican Republic"])
print(staty.loc[["Czech Republic", "Slovakia"], "capital"])
print(staty.loc[["Poland", "Slovakia", "Austria", "Germany"], ["capital", "gini", "population"]])

print(staty[["population", "area"]]) #if more than one variable, use double brackets [[ ]]


populace = staty["population"] #prevod do typu serie
print(populace.sum())

pidistaty = (staty[staty["population"] < 1000]) #return only countries will less than 1000 population
print(pidistaty[["area", "population"]]) #chybejicic data u rozhlohy - tohle by se melo filtrovat, cleaning data is important

EU_high_population = staty[(staty["population"] > 20_000_000) & (staty["region"] == "Europe")]
print(EU_high_population) #dve podminky, zeme v EU a s populaci vetsi nez 20mil,
                            obe podminky jsou spojene znakem & (and)

important_states = staty[(staty["population"] > 2_000_000_000)| (staty["area"] > 3_000_000)]
print(important_states) #jedna ze svou podminek musi byt pravdiva:
                        # zeme z vetsi populaci nez 1 miliarda NEBO rozloha vetsi nez 3mil

Wes_east_Europe = staty[staty["subregion"].isin(["Western Europe", "Eastern Europe"])]
#filtruje podle subregionu, pouze ty radky ktere maji Western Europe a Easterm Europe
print(Wes_east_Europe)