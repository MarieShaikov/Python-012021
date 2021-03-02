#Balík

#Uvažuj, že navrhuješ software pro zásilkovou společnost.

#Vytvoř třídu Package, která bude mít tři atributy - address, weightInKilos a delivered.
# První dva atributy nastav pomocí parametrů funkce __init__.
# Parametr delivered nastav na začátku jako False.
#Připoj ke třídě funkci deliver, která změní hodnotu parametru delivered na True.
#Přidej funkci getInfo, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
#Zkus si vytvořit nějaké objekty ze třídy Package a ověř, že vše funguje.


class Package:
    def __init__(self, address, weight):
        self.address = address
        self.weight = weight
        self.delivered = False


    def deliver(self):
        self.delivered = True

    def get_info(self):
        if self.delivered:
             return f"adresa {self.address} with weight {self.weight} was delivered."
        return f"adresa {self.address} with weight {self.weight} was not delivered."

balik = Package('Brno', 250)
print(balik.get_info())
balik.deliver()
print(balik.get_info())