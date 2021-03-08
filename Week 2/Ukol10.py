# Klíč k úspěchu
# Obchodníci v naší softwarové firmě používají jednoduchý systém,
# aby odhadli šanci na úspěch potenciální zakázky. Každé zakázce přiřadí body od 0 do 10 a platí:

# Odvětví: Firma nejlépe prodává do automotive, o něco hůře do retailu.
# Pokud potenciální zákazník podniká v automotive, přičti 3 body,
# pokud v retailu, přičti 2 bod, jinak 0.

# Obrat: Firma nejlépe prodává zákazníkům se středním obratem.
# U malých většinou neuspěje, u velkých občas ano. Pokud má firma obrat menší než 10 mil.
# Euro, přičti 0. Pokud je mezi 10 a 1 000 mil. Euro, přičti 3 body, jinak 1 bod.

# Země: Firma je nejúspěšnější v Česku a na Slovensku (2 body),
# o něco méně v Německu a ve Francii (1 bod). Ostatním zemím dej 0.

# Konference: Firma loni pořádala odbornou konferenci pro zákazníky.
# Pokud se zákazník konference účastnil, přičti 1 bod, jinak 0.

# Newsletter: Firma též rozesílá newsletter o svém produktu.
# Pokud zákazník newsletter odebírá, přičti 1 bod.

# Napiš funkci, které bude mít 5 parametrů, které reprezentují zadaná kritéria.
# Poslední dvě kritéria zadej jako nepovinná s výchozí hodnotou False.
# Funkce vrátí šanci na získání zakázky jako řetězec.

orders = {"industry": "automotive", "money": 12, "country": "Czechia", "conference": True, "newsletter": False}


def chance_of_success(industry, money, country, conference=False, newsletter=False):
    total = 0
    if industry == "automotive":
        total += 3
    elif industry == "retail":
        total += 2
    if money <= 10:
        total += 0
    elif 10 <= money <= 1000:
        total += 3
    else:
        total += 1
    if country in ["Czechia", "Slovakia"]:
        total += 2
    elif country in ["Germany", "France"]:
        total += 1
    if conference:
        total += 1
    if newsletter:
        total += 1
    return total

x = chance_of_success("automotive", 5, "Czechia", conference=True, newsletter=True)
print(x)

if x <= 5:
    print('small chance to win the order')
elif 6 <= x <= 8:
    print("50/50")
else:
    print("high chance to win the order")


# Pokud má zakázka méně než 5 bodů, šance na záskání je malá.
# Pokud má zakázka 6 až 8 bodů, šance na získání je střední.
# Pokud má zakázka více bodů, šance na získání je vysoká.
# Body přidělují podle následujících kritérií:
