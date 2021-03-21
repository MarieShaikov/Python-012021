# Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.
#
# Datum	Cena
# 1. 7. 2021 - 10. 8. 2021	250 Kč
# 11. 8. 2021 - 31. 8. 2021	180 Kč
# Mimo tato data je středisko zavřené.
#

from datetime import datetime

def price_cinema(date_ticket):

    first= datetime(2021,7,1)
    second= datetime (2021,8,10)
    third=datetime(2021,8,11)
    fourth=datetime(2021,8,31)

    if (date_ticket > first) and (date_ticket < second):
        return 250
    elif (date_ticket > third) and (date_ticket < fourth):
        return 180
    else:
        return("The cinema is closed")


date_ticket = "02.07.2021"
number = 2

x = datetime.strptime(date_ticket, '%d.%m.%Y')
print(price_cinema(x))


#x = input(f" Date is: {date}, number of people: {number})


# Tvůj program se nejprve zeptá uživatele na datum a počet osob,
# pro které uživatel chce vstupenky koupit. Uživatel zadá datum ve středoevropském formátu.
# Převeď řetězec zadaný uživatelem na datum pomocí funkce datetime.strptime().
#
# Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v té době uzavřené.
# Pokud je letní kino otevřené, spočítej a vypiš cenu.
#
# Data lze porovnávat pomocí známých operátorů <, >, <=, >=, ==, !=.
# Tyto operátory můžeš použít v podmínce if. Níže vidíš příklad porovnání dvou dat.
# Program vypíše text "První datum je dřívější než druhé datum.".
#
# from datetime import datetime
# prvni_udalost = datetime(2021, 7, 1)
# druha_udalost = datetime(2021, 7, 3)
# if prvni_datum < druhe_datum:
#   print("Druhá událost se stala po první události")