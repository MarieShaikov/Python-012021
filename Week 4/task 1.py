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

class PartTimeEmployee(Employee):
    def __init__(self, name, position, workload):
        super().__init__(name, position)
        self.workload = workload

#super function is connecting the part time emplopyee to Employee class,
# it takes the common variables from Employee and insert it to the class PartTimeEmployee,
# so we dont have to copy the same code for other class (note that workload is specific to PartTimeEmployee,
# needs to be definided indivudally for the class of PartTimeEmployee