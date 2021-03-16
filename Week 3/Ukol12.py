# Půjčení auta
# Pokračuj ve své práci pro autopůjčovnu, kterou jsi začala v příkladu 11.
#
# Třídě Auto přidej funkci pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr.
# Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu,
# který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla".
# Pokud je vozidlo již půjčené,
# vrátí text "Vozidlo není k dispozici".

class Car:
    def __init__(self, reg_number, car_type, km_number, available=True):
        self.reg_number = reg_number
        self.car_type = car_type
        self.km_number = km_number
        self.available = available

    def car_rent(self):
        if self.available:
            self.available = False
            return "This is a confirmation that car rent is available"
        else:
            return "The car is currently not available for rent"

    def get_info(self):
        if self.available:
            return f"Car with registration number {self.reg_number}, " \
               f" {self.car_type}, {self.km_number} number of kilometers is currently available."
        return f"Car with registration number {self.reg_number} " \
               f"{self.car_type}, {self.km_number} number of kilometers is currently not available."

car1 = Car("4A2 3020", "Peugeot 403 Cabrio", 47534, available=False)
car2 = Car("1P3 4747", "Škoda Octavia", 41253)

while True:
    x = input("Which car type would you like to rent?")
    if x == "Peugeot":
        print(car1.get_info(), car1.car_rent())
    elif x == "Skoda":
        print(car2.get_info(), car2.car_rent())


#Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a
# typ vozidla) jako řetězec.
#
# Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel
# může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí
# funkce get_info() a následně použij funkci pujc_auto.
#
# Dotaz na uživatele a výpis výsledků si v programu zkopíruj, abys dokázala otestovat,
# že funkce nedovolí půjčit stejné auto dvakrát.