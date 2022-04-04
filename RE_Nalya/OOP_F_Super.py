class Computer:    #Perant
    def __init__(self, computer, ram, ssd): #Параметры
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

# Если создать дочерний класс 'Laptop', то будет доступ к свойству базового класса благодаря функции Super()

class Laptop(Computer):    #child
    def __init__(self,computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model

# Создаем объект и передаем аргументы(то что мы знаем уже)
lenovo = Laptop('Lenovo', 2, 512, 'l420')   # create an object


print('This computer is: ',lenovo.computer )
print('This computer has ram of: ', lenovo.ram)
print('This computer has ssd of: ', lenovo.ssd)
print('This is computer has this model: ', lenovo.model)






