class Draw:
    color = 'red'  #переменная класса
    form = 'circle'

    def changecolor(self,newcolor):  #метод класса self нужен что бы сказать методу,что он будет работать с объектами этого класса
        self.color = newcolor  # возъмем color и присвоим объекту класса (self) newcolor, который передадим методу

    def changeform(self,newform):
        self.form = newform

obj1 = Draw()
obj2 = Draw()  # Объекты класса

print(obj1.color, obj1.form)
print(obj2.color, obj2.form)

obj1.changecolor('green') #вызываем метод и изменяем цывет первого объекта
obj2.changecolor('blue') # изменение цвета второго объекта
obj2.changeform('oval') # изменение формы второго объекта

print(obj1.color, obj1.form)
print(obj2.color, obj2.form)