# Vrácení auta
# Pokračuj ve své práci pro autopůjčovnu z příkladu 11 a příkladu 12.
# Přidej třídě Auto funkci vrat_auto(), která bude mít (krom obligátního self) 2 parametry, a
# to je stav tachometru při vrácení a počet dní, po které zákazník auto používal.
# Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

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

    def car_return(self, days):
        if days <= 7:
            return "The price for rent is", (300 * days)
        else:
            return "The price for rent is", (400 * days)


car1 = Car(f"4A2 3020", "Peugeot 403 Cabrio", 47534)
car2 = Car(f"1P3 4747", "Škoda Octavia", 41253)

x = input("Which car type do you want to rent?")
if x == "Peugeot":
    print(car1.get_info(), car1.car_rent())
elif x == "Skoda":
    print(car2.get_info(), car2.car_rent())


speedometer = int(input("How many km have you driven?"))
days = int(input('How many days did you rent the car for?'))


if x == "Peugeot":
    print(car1.car_return(days))

if x == "Skoda":
    print(car2.car_return(days))



# Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník
# celkem auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle.
# Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return.
#
# Na konec programu (mimo třídu) přidej dotaz na uživatele, kolik kilometrů zákazník ujel a
# jak dlouho ho měl půjčené. Poté vypiš informaci o ceně.