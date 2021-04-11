import pandas

jmena = pandas.read_csv('jmena.txt')
studenti1 = pandas.read_csv('studenti1.txt')
studenti2 = pandas.read_csv('studenti2.txt')

students = pandas.concat([studenti1, studenti2], ignore_index=True)
print(len(students[students['ročník'].isnull()])) #students who donts study

print(students[students.dropna(subset["ročník", "kruh"])]) #clean all data from those who dont study anymore and those who study distance


# Načtěte dva datové sety studentů do oddělených pandas DataFrame a pomocí funkce concat je spojte do jednoho setu.

# Pokud studentovi chybí ročník, znamená to, že již nestuduje.
#
# Pokud mu chybí číslo skupiny,znamená to, že jde o dálkového studenta. Kolik studentů v datovém setu již nestuduje a kolik jsou dálkoví studenti?
# Vyčistěte data od studentů, kteří nestudují nebo studují jen dálkově.

# Nadále budeme pracovat pouze s prezenčními studenty.
# Zjistěte, kolik prezenčních studentů je v každém z oborů.

print(students.groupby("obor")["kruh"].count())

# Zjistěte průměrný prospěch studentů v každém oboru.

print(students.groupby("obor")["prospěch"].mean())


# Načtěte datový set s křestními jmény. Proveďte join s tabulkou studentů tak,
# abychom věděli pohlaví jednotlivých studentů.

jmena = pandas.read_csv('jmena.txt')
merged = pandas.merge(students, jmena, how="left", on=["jméno"])

# Zjistěte, zda na naší fakultě studují IT spíše ženy nebo spíše muži.