
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
# Uvažuj, že zpracováváš analýzu pro softwarovou firmu. Firma má kanceláře v Praze, Plzni a Liberci.
# Seznam zaměstnanců pro jednotlivé kanceláře najdeš v souborech zam_praha.csv, zam_plzeň.csv a zam_liberec.csv.

import pandas
praha = pandas.read_csv('data_praha.csv')
plzen = pandas.read_csv('data_plzeň.csv')
liberec = pandas.read_csv('data_liberec.csv')
platy = pandas.read_csv("data_platy.csv")

# Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame). Ke každé tabulce přidej nový
# sloupec mesto, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
praha["City"] = "Praha"
plzen["City"] = "Plzen"
liberec["City"] = "Liberec"


# Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
employees = pandas.concat([praha, plzen, liberec],ignore_index=True)
print(employees)

# Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join) s
# platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.

new_table = pandas.merge(platy, employees, on=["cislo_zamestnance"])
print(new_table)

# Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor,
# znamená to, že v naší firmě již nepracuje.

# Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.

print(new_table.groupby('City')["plat"].mean())
# Liberec    43775.000000
# Plzen      44792.857143
# Praha      43295.238095