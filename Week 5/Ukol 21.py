# Stáhni si soubor twlo.csv, který obsahuje informace o vývoji ceny akcie firmy Twilio od začátku roku 2020. Soubor obsahuje informace o otevírací, minimální, maximální a uzavírací ceně za každý den.
#
# Stažení souboru pomocí wget:
#

#("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")

import pandas
companies = pandas.read_csv('Ukol21_data.csv')

# Zjisti, kolik má soubor řádek a kolik sloupců.
print(companies.info) # --> [302 rows x 6 columns]

# Podívej se na 5 řádků s cenami na začátku souboru, využij k tomu funkci iloc i funkci head().

print(companies.head)

print(companies.head(n=5)) #calling the first 5 rows for all variables using head
print(companies.iloc[:5]) #calling the first 5 rows for all variables using iloc


# U akcií nás zajímají především nejnovější ceny. Podívej se na poslední řádek souboru.
# Tentokrát využij způsob dle vlastního výběru :-)

print(companies.tail(n=1))

# Dobrovolný doplněk
#
# Tato část je jen doplnění, k získání bodu je potřeba zpracovat dotazy výše :-)
#
# Počet řádků ulož do proměnné pocet_radku jako číslo.
# Pokud funkci iloc zadáš číslo řádku i číslo sloupce, odkazuješ se na jednu konkrétní hodnotu.
# Pandas ti tuto hodnotu vrací jako číslo. Načti si tedy první hodnotu zavírací ceny (sloupec Close)
# v souboru a poslední hodnotu zavírací ceny v souboru.
# Vypočítej, o kolik procent se zvýšila hodnota akcie.

number_row = int(len(companies))
first_Close = (companies.iloc[1, 5])
last_Close = (companies.iloc[301, 5])
increase_value = (last_Close - first_Close)/first_Close * 100
print(increase_value) # the value has increased by 257%

# Vyber si sloupec s maximální cenou akcie (sloupec High) za jednotlivé dny pomocí loc nebo iloc jako sérii.
# Na sloupec použij funkci .max(), abys zjistila maximální zaznamenanou cenu akcie za celé období.
# Obdobným způsobem použij funkci .min() na sloupec Low. Z těchto hodnot zjistíš maximální rozsah obchodní ceny akcie,
# což je základ jednoho z akciových ukazatelů (price range).

max = (companies.High.max()) # max = 457.3
min = (companies.Low.min()) # min = 68
price_range = max - min
print(price_range) # price range is 389.2
