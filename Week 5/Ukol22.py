# Stáhni si soubor character-deaths.csv, který obsahuje informace o smrti některých postav z prvních pěti
# knih románové série Píseň ohně a ledu (A Song of Fire and Ice).
#
# Stažení souboru pomocí wget:
#
#"https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv"
# Pozn. Úkoly se týkají zcela nevýznamných postav, proto je riziko spoileru minimální :-)

# Načti soubor do tabulky (DataFrame) a nastav sloupec Name jako index. # Zobraz si sloupce, které tabulka má. Posledních pět sloupců tvoří zkratky názvů knih a informace o tom,
# # jestli se v knize postava vyskytuje.

import pandas
df = pandas.read_csv('Ukol22_data.csv')
df = df.set_index("Name") # name as index
print(df.head)

# Použij funkci loc ke zjištění informací o smrti postavy jménem "Hali".
print(df.loc["Hali", "Death Year"]) # Death Year  298.0

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".

print(df.loc["Gevin Harlaw":"Gillam"])

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce Death Year.

print(df.loc["Gevin Harlaw":"Gillam", "Death Year"])

# Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom, v
# jakých knihách se postava vyskytuje, tj. vypiš všechny sloupce mezi GoT a DwD.

print(df.loc["Gevin Harlaw":"Gillam", "GoT":"DwD"])