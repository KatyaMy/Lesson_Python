class Cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        print(f'Cat {self.name} - is being initialized and says Meow!')

    def say_meow(self):
        print(f'{self.name} says Meow!')

    def print_name(self):
        print('This is', self.name)

    def print_age(self):
        print(f'{self.name} is {self.age} y.o')

    def print_weight(self):
        print(f'{self.name} is {self.weight} lbs')

    def eat_a_lot(self,food = 'food'):
        self.weight += 0.80
        print(f'{self.name} ate {food} and gained some pound')

#
black_cat = Cat("Tom", 2, 8)
print(black_cat)
black_cat.print_name()
black_cat.print_age()
black_cat.print_weight()
#
# black_cat.eat_a_lot("Chicken")
# black_cat.print_weight()
#Объекты класса CAT (black_cat and Gray_cat)
gray_cat = Cat('Lucky', 3, 14)
print(gray_cat)


