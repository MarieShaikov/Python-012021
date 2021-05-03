# Výplata
# Uvažujme nyní opět třídu Employee, kterou jsme si ukázali v lekci.
# Pro zjednodušení nyní nebudeme pracovat s dovolenou, proto nám stačí třída, která je v ukázce níže.
#
class Employee:

    def __init__(self, name, position, salary, children):
        self.name = name
        self.position = position
        self.salary = salary
        self.children = children

    def get_info(self):
        return f"{self.name} works as {self.position}."

    def get_tax(self):
        return self.salary * 0.15 - (self.children * 1500)

    def netto(self):
        return self.salary - self.get_tax()


c = Employee("George", "teacher", 80_000, 2)
print(c.get_info())
print("This is your netto salary: ", c.netto())

# Nyní se budeme zabývat platem. Přidej třídě atribut salary (výše hrubého platu) a
# children (počet dětí), jehož výši nastavíš ve funkci __init__().

# Dále přidej funkci get_net_salary(), která vypočte a vrátí výši čisté mzdy.
# Uvažuj zjednodušený výpočet: sazba daně je 15 % a sleva na jedno dítě 1500 Kč. Vzorec pro výpočet daně
# tedy je: daň = hrubá mzda * 0.15 - počet dětí * 1500. Funkce vrátí výši čisté mzdy, tj. čistá mzda = hrubá mzda - daň.
#
# Pokročilejší verze: Pokud máš zájem, můžeš zkusit pokročilejší verzi. Rozlož výpočet do dvou funkcí.
# Přidej funkci get_tax(), která vypočte výši daně, a poté funkci get_net_salary().
# Výpočet daně bude ve funkci get_tax(). Funkce get_net_salary() zavolá funkci get_tax(),
# aby zjistila výši daně, a poté vrátí čistou mzdu. Volání funkce proveď pomocí klíčového slova, tj. např.:
#
# net_salary = self.salary - self.get_tax()
# Bod samozřejmě získáš za obě verze :-)