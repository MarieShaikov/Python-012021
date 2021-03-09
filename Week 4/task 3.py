Zkušební doba

U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.

Rozšiř funkci __init__ třídy Employee o parametr probation,
který bude typu bool. Tuto hodnotu ulož jako atribut třídy Employee.
Uprav funkci getInfo. Pokud je zaměstnanec ve zkušební době, přidej k
jeho/jejímu výpisu text Je ve zkušební době.

class Employee:
    def get_info(self):
        return f"{self.name} working on the position {self.position}"

    def __str__(self):
        self.name = name
        self.position = position
        self.holidays = 25  # vacation is equal for all employees
        

    def __init__(self, name, position, probation):
    super().__init__(self, name, position)
        self.probation = probation

    return f"{self.name} working on the position {self.position} {self.probation}"
