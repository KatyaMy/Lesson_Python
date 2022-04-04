# class Polygon:
#     def get_sides(self):
#         pass
#
#     sides_count = None
#
#
# class Triangle(Polygon):
#      def __init__(self):
#          self.sides_count = 3
#
#      def get_sides(self):
#         print(f"It has {self.sides_count} sides")
#
#
# class Pentagon(Polygon):
#     def __init__(self):
#         self.sides_count = 5
#
#     def get_sides(self):
#         print(f"It has {self.sides_count} sides")
#
#
# Poly = Polygon()
# Poly.get_sides()
#
# T = Triangle()
# T.get_sides()
#
# P = Pentagon()
# P.get_sides()


class Animal:
    def __init__(self, name):
        self.name = name
        self.weight = 0

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.weight = 10

    def speak(self):
        print("woof")


Dog = Dog('DOg')
Dog.speak()
print(Dog.weight)

class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.weight = 5

    def speak(self):
        print("myyuu")


Cat = Cat('Cat')
Cat.speak()
print(Cat.weight)