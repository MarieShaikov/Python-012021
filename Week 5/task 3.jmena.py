import pandas
jmena = pandas.read_csv('jmena.csv')

# Datový soubor obsahuje následující sloupečky
#
# jméno - křestní jméno
# četnost - počet obyvatel ČR mající toto jméno
# věk - průměrný věk nositelů jména
# pohlaví - zda je jméno mužské či ženské
# svátek - datum, kdy má dané jméno svátek
# původ - původ jména
# Vyřešte následující úkoly.
#
# Vypište na konzoli informace o jménu Jiří.
# Vypište na konzoli informace pro jména Martin, Zuzana a Josef.
# Vypište na konzoli informace o všech nejčastějších jménech až po Jiřího.
# Vypište pouze průměrné věky osob mající jména mezi Martinem a Terezou.
# Vypište průměrný věk a původ pro všechna jména od Libora dolů.
# Vypište sloupečky mezi věkem a původem pro všechna jména v tabulce.

#print(jmena.set_index("jméno"))

jmena = jmena.set_index("jméno") #index is key, key which will find values in rows in a specific columns, finds value in dataframe

print(jmena.loc["Jiří"])
print(jmena.loc[["Jiří", "Martin", "Zuzana", "Josef"]])
print(jmena.loc[:"Martin"])
print(jmena.loc["Martin":"Tereza", "věk"])
print(jmena.loc["Libor": , ["věk", "původ"]])
print(jmena.loc[:,"věk" : "původ"])

# Vypiš všechny řádky se jmény, jejichž nositelé mají průměrný věk vyšší než 60.
# Vypiš pouze jména z těch řádků, kde četnost je mezi 80 000 a 100 000.
# Vypiš jména a četnost pro jména se slovanským nebo hebrejským původem. Kolik takových jmen je?
# Vypiš všechna jména, která mají svátek první 3 dny v únoru.


old = jmena[(jmena["věk"] > 60 )]
print(old)

ukol2 = jmena[(jmena["četnost"] < 80_000) & (jmena["četnost"] < 100_000)]
print(ukol2)

ukol3 = jmena[jmena["původ"].isin(["slovanský", "hebrejský"])]
print(ukol3)

