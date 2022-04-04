class Draw:
    color = 'red'
    form = 'circle'

    def changecolor(self,newcolor):
        self.color = newcolor

    def changeform(self,newform):
        self.form = newform

obj1 = Draw()
obj2 = Draw()

print(obj1.color, obj1.form)
print(obj2.color, obj2.form)

obj1.changecolor('green')
obj2.changecolor('blue')
obj2.changeform('oval')

print(obj1.color, obj1.form)
print(obj2.color, obj2.form)