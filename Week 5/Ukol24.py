# Stáhni si soubor temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
#
#("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
# Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.

import pandas
df = pandas.read_csv('Ukol24_data.csv')
print(df.iloc[:4])

# Dále napiš následující dotazy:
#
# Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být?

task1 = df[df["City"] == "Prague"]
print(task1)
#it seems that the values are not in Celsia but in fahrenheit

# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.

task2 = df[df["AvgTemperature"] > 80]
print(task2)

# Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region)
# Evropa (Europe).

task3 = df[(df["AvgTemperature"] > 60) & (df["Region"] == "Europe")]
print(task3)

# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.

extreme_values = df[(df["AvgTemperature"] > 80) | (df["AvgTemperature"] < -20)]
print(extreme_values)
#there are actually no avgTemper. below - 20


# Pokročilá varianta

# Nainstaluj si modul pytemperature a zkus si vytvořit nový sloupec, který bude obsahovat průměrnou templotu ve
# stupních Celsia. Ve svém programu nejprve proveď import modulu pytemperature. Nový sloupec pak přidáš do
# tabulky tak, že nalevo od = vložíš tabulku a název nového sloupce do hranatých závorek.
# Napravo pak můžeš provádět výpočty pomocí již existujících sloupců. Můžeš např. použít funkci f2c z
# modulu pytemperature, která převede teplotu ze stupňů Fahrenheita na stupně Celsia.
#
# import pytemperature
# df["AvgTemperatureCelsia"] = pytemperature.f2c(df["AvgTemperature"])
# Nyní můžeš zpracovat následující příklady:
#
# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.
# Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu
# (sloupec Region) Evropa (Europe).
# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů.
# Jsou některé hodnoty podezřelé?