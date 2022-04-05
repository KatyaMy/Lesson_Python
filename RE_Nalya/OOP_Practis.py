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
        self.nameDirector = nameDirector
        self.salary = salary
        self.nameEmployee = nameEmployee
        self.position = position
        Macdonalds.margin = ( self.salary * 20)/100


    def displayEmployee(self):
        print('nameDirector: ',self.nameDirector, 'Employee: ',self.nameEmployee, 'Position: ',self.position, 'Salary: ',self.salary,'$')


city_California = Macdonalds('M.Madysson', 'Sam', 'Cook', 4500)

city_Pensilvania = Macdonalds('J. Smitt', 'Amanda', 'cashier', 3500)

city_California.displayEmployee()
print(f'In California Margin + 20 % = {Macdonalds.margin} ')

city_Pensilvania.displayEmployee()
print(f'NOT Margin')

