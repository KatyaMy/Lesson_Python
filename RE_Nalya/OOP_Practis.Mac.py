"""Задание:
Создать сеть Макдональдс, где в главном классе 
будет содержаться - неизменяемое имя директора
- зарплата сотрудника
- имя сотрудника
- тип занятости
Отделение в Пенсильвании и Калифорнии
-В Пенсильвании зарплата без наценок
-В Калифорнии +20 процентов"""''

class Macdonalds:

    marginCali = 0

    def __init__(self, nameDirector, nameEmployee, position, salary):
        self.__nameDirector = nameDirector
        self.salary = salary
        self.nameEmployee = nameEmployee
        self.position = position
        Macdonalds.margin = ( self.salary * 20)/100


    def displayEmployee(self):
        print(f'nameDirector: {self.__nameDirector},\n' 
              f'Employee: {self.nameEmployee},\n',
              f'Position: {self.position},\n'
              f'Salary: {self.salary},\n')


city_California = Macdonalds('M.Madysson', 'Sam', 'Cook', 4500)
city_California.displayEmployee()
print(f'In California Margin + 20 % = {Macdonalds.margin} ')


city_Pensilvania = Macdonalds('M.Madysson','Amanda', 'cashier', 3500)
city_Pensilvania.displayEmployee()
print(f'NOT Margin')







#II.
# class Macdonalds:
#
#     director = 'Jhon Pit'
#
#     def __init__(self, nameEmployee, position, salary):
#
#         self.salary = salary
#         self.nameEmployee = nameEmployee
#         self.position = position
#
#     def printe_Employee(self):
#         print(f"Director Name is: {Macdonalds.director},\n"
#               f"Employee name is: {self.nameEmployee},\n"
#               f"Employee position: {self.position},\n"
#               f"Employee salary: {self.salary}")
#
#
# class PA_Mac(Macdonalds):
#     def __init__(self, nameEmployee, position, salary):
#         super().__init__(nameEmployee, position, salary)
#
# class CA_Mac(Macdonalds):
#     def __init__(self, nameEmployee, position, salary):
#         super().__init__(nameEmployee, position, salary * 1.2,)
#
#
# employeePA = PA_Mac('Piter', 'Cook', 3800)
# employeeCA = CA_Mac('Marta', 'Bar', 5000)
#
# employeePA.printe_Employee()
# employeeCA.printe_Employee()
