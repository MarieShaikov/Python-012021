# Stáhni si soubor country_vaccinations.csv o průběhu očkování proti nemoci COVID-19.
#
#("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
# Dále napiš následující dotazy:
#
import pandas
df = pandas.read_csv('Ukol23_data.csv')
print(df.head)

# Dotaz na počty očkovaných (sloupec total_vaccinations) v jednotlivých státech dne 2021-03-10
# (s datem pracuj úplně stejně jako s řetězcem, tj. nevyužívej modeul datetime, ale vlož do dotazu přímo řetězec).

total = df[df["date"] == "2021-03-10"]['total_vaccinations']
print(total)

# Dotaz na řádky, kde 2021-03-10 bylo naočkováno více než 1 mil. obyvatel.

vaccination = df[(df["date"] == "2021-03-10") & (df["total_vaccinations"] < 1_000_000)]['total_vaccinations']
print(vaccination)

# Podíváme se na extrémní hodnoty. Napiš dotaz na řádky, kde za daný den naočkování více než 100 tisíc lidí
# nebo naopak méně než 100 lidí.

high_values = df[df["daily_vaccinations"] > 100_000]['daily_vaccinations']
low_values = df[df["daily_vaccinations"] < 100_000]['daily_vaccinations']
print(high_values, low_values)



# Dobrovolný doplněk
#
# Vypiš informace o očkování za dny 2021-03-10 a 2021-03-11 pro státy United Kingdom, Finland a Italy.
# Použij např. funkci isin().
# Vypiš informace o očkování pro Japan mezi daty 2021-03-03 a 2021-03-09.
# Data v tomto formátu můžeš porovnávat pomocí operátorů >= a <= jako řetězce, tj.
# opět nemusíš použít modul datetime.

