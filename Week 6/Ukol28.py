# import wget
#
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")
# V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali.
# Zkusme nyní zpracovat podobné úlohy pomocí pandas.


# Načti data ze souboru do tabulky.
import pandas
states = pandas.read_json("Ukol28_data.json")

# Vyfiltruj státy, které leží v Evropě.
states = states.set_index("region")
Europe_states = states.loc["Europe"]
print(Europe_states)

# Zjisti počet států v jednotlivých subregionech Evropy.
Europe_subregion = Europe_states.groupby(['subregion', "region"])["name"].count()
Europe_subregion.name = "Count_Europe_subregion"
print(Europe_subregion)

#Result:
# subregion        region
# Eastern Europe   Europe    11
# Northern Europe  Europe    16
# Southern Europe  Europe    17
# Western Europe   Europe     9

# Zjisti cekový počet obyvatel v jednotlivých subregionech Evropy.
population_subregion = Europe_states.groupby(["subregion"])["population"].sum()
population_subregion.name = "Europe_subregion_population"
print(population_subregion)


# Rozšíření zadání

# V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali.
# V souboru gdp.csv jsou dále informace o hrubém domácím produktu (Gross Domestic Product - GDP) států za
# roky 2017-2019 ze Světové banky.
#
# Načti informace ze souborů do tabulek. Z tabulky s GDP odeber státy, které nemají kompletní informace GDP
# (tj. ponech pouze státy, které mají kompletní data za všechny tři roky).

import pandas
gdp = pandas.read_csv("Ukol28_data2.csv").dropna()
print(gdp.iloc[:4])

# Propoj obě tabulky podle třípísmenného kódu států.
merged_tables = pandas.merge(gdp, states, left_on="Country Code", right_on="alpha3Code", suffixes=(False, False))
print(merged_tables)


# Spočti celkové HDP za rok 2019 a celkový počet obyvatel za jednotlivé subregiony.

print(merged_tables["2019"].sum()) #celkové HDP za rok 2019

subregion_population = merged_tables.groupby(["subregion"])["population"].sum()
print(subregion_population) #celkový počet obyvatel za jednotlivé subregiony


# Projdi si subkapitolu o počítaných sloupcích (část o podmínených sloupcích není nutné číst). K tabulce,
# kterou jsi vytovřila v předchozím kroku, vypočti GDP v roce 2019 na obyvatele, tj. přidej sloupec s velikostí
# GDP v roce 2019 vydělenou počtem obyvatel daného subregionu.

merged_tables["GDP_perCapita"] = merged_tables["2019"] / merged_tables["population"]
subregion_GDP_perCapita = merged_tables.groupby(["subregion"])["GDP_perCapita"].sum()
print(subregion_GDP_perCapita.head)