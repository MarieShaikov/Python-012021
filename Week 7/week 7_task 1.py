import pandas
staty = pandas.read_json('staty.json')
staty = staty.set_index("name")

staty["population_density"] = staty['population']/staty["area"]

#staty = staty.sort_values("population_density") #orders automaticly from lowest values to highest

staty = staty.sort_values("population_density", ascending=False)
print(staty.head())