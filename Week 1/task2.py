class Employee:
    def take_holiday(self, days):
        if self.holidays >= days:
            self.holidays = self.holidays - days
            return "Holiday approved"
        else:
            return f" {self.name} can take only {self.holidays}"


george = Employee('George k', 'editor')
print(george.take_holiday(10))
