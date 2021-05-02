# import wget
#
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")
# Pokračuj ve své práci pro softwarovou firmu. Ze souboru vykazy.csv načti informace o výkazech na projekty
# pro jednoho vybraného zákazníka.
#
# Načti data ze souboru a ulož je do tabulky.
# Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.

import pandas
projects = pandas.read_csv('Ukol27_data.csv')
print(projects.iloc[:3])
print(projects.groupby('project')["hours"].sum())
#Result

# #F30    21.5
# JL9     2.1
# TE1    16.0
# W05    30.5
# YLI    31.0


# Dobrovolný doplněk

# Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení.
# Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře, tj. spočítej celkový počet hodin
# vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.

import pandas
praha = pandas.read_csv('data_praha.csv')
plzen = pandas.read_csv('data_plzeň.csv')
liberec = pandas.read_csv('data_liberec.csv')
platy = pandas.read_csv("data_platy.csv")

praha["City"] = "Praha"
plzen["City"] = "Plzen"
liberec["City"] = "Liberec"

employees = pandas.concat([praha, plzen, liberec],ignore_index=True)
offices_stats = pandas.merge(projects, employees,left_on='emloyee_id', right_on='cislo_zamestnance', suffixes=(False, False))
total = (offices_stats.groupby(['City', "project"])['hours'].sum())
print(total)

#Result:

#City     project
# Liberec  TE1        10.8
#          W05         5.4
#          YLI        11.8
# Plzen    F30        10.3
#          YLI         5.3
# Praha    F30        11.2
#          JL9         2.1
#          TE1         5.2
#          W05        25.1
#          YLI        13.9
