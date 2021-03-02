class Employee:
    def get_info(self):
        return f"{self.name} working on the position {self.position}"

    def __str__(self):
        return self.name
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.holidays = 25 #vacation is equal for all employees

george = Employee('George Nufi', 'dirty worker')
klara = Employee('`klara noava', 'editor')
print(george)


#george.name =
#george.position =
#george.get_info()
#print(george.get_info())




