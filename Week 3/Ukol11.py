# Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:
#
# Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
# 4A2 3020	Peugeot 403 Cabrio	47534
# 1P3 4747	Škoda Octavia	41253
# Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:
#
# registrační značka automobilu,
# značka a typ vozidla,
# počet najetých kilometrů,
# informaci o tom, jestli je vozidlo aktuálně volné (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).
# Vytvoř funkci __init__ pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej
# jako parametry funkce __init__ a ulož je jako atributy objektu.
# Poslední atribut nastav jako True, tj. na začátku je vozidlo volné.
#
# Vytvoř objekty, které reprezentují všechny automobily půjčovny.

class Car:
    def __init__(self, reg_number, car_type, km_number,available = True):
        self.reg_number = reg_number
        self.car_type = car_type
        self.km_number = km_number
        self.available = available

    def get_info(self):
        if self.available:
            return f"Car with registration number {self.reg_number}, " \
               f" {self.car_type}, {self.km_number} number of kilometers is currently available."
        return  f"Car with registration number {self.reg_number} " \
               f"{self.car_type}, {self.km_number} number of kilometers is currently not available."

cars = Car("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
print(cars.get_info())


# 4A2 3020	Peugeot 403 Cabrio	47534
# 1P3 4747	Škoda Octavia	41253

