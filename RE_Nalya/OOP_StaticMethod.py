class Employee:
    empCount = 0


    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

        @staticmethod
        def displayCount():
            print('Total Employee %d' % Employee.empCount)
            # %d is the format specifier user to print integers or number

    def displayEmployee(self):
        print('Nmae: ', self.name, 'Salary: ', self.salary)


emp1 = Employee('Zara', 2000)
emp2 = Employee('Manni', 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print('Total Employee %d' % Employee.empCount)
