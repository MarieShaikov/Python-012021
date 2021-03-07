#Zkušební doba

#U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.
#Rozšiř funkci __init__ třídy Employee o parametr probation, který bude typu bool.
# Tuto hodnotu ulož jako atribut třídy Employee.
#Uprav funkci getInfo. Pokud je zaměstnanec ve zkušební době, přidej k
#jeho/jejímu výpisu text Je ve zkušební době.


#FINISH THE EXERCISE

class Employee:
    def get_info(self):
        return f"{self.name} working on the position {self.position}"

    def __str__(self):
        return self.name

    def __init__(self, name, position, probation):
        self.name = name
        self.position = position
        self.holidays = 25  # vacation is equal for all employees
        self.probation = probation


george = Employee('George Nufi', 'worker')
klara = Employee('`klara nova', 'editor')
print(george)