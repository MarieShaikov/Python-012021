# Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých
# městech v listopadu 2017.
#
# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
# Pokud jsi v minulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve stupních Celsia.
#
import pandas
temperature = pandas.read_csv("Ukol29_data.csv")
print(temperature.head)

# Vyfiltruj si informace o teplotách 13. listopadu 2017.

temp_13 = temperature[temperature["Day"] == 13]
print(temp_13)

# Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
temperature.drop(temperature.index[temperature['AvgTemperature'] == -99], inplace=True)
print(temperature)


# Vypočti počet dat, které máš pro daný den za jednotlivé regiony.
count = (temperature.groupby(["Region", "Day"])["Day"].count())
print(count)

# Vypočti průměrnou teplotu za jednotlivé regiony.
average = (temperature.groupby(["Region"])["AvgTemperature"].mean())
print(average)

# Vypočti maximální a minimální teplotu v každém regionu.
max = (temperature.groupby(["Region"])["AvgTemperature"].max())
print(max)

min = (temperature.groupby(["Region"])["AvgTemperature"].min())
print(min)

