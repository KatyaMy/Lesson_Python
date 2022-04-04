class Person:
    def __init__(self, name, dob, height, gender):
        self._name = name
        self.__dob = dob
        self.height = height
        self.gender = gender

    def get_name(self):
        return self._name

    def get_dob(self):
        return self.__dob

    def set_dob(self, new_dob):
        self.__dob = new_dob

persone_one = Person('Joth','May 3',2000, "M")

print(persone_one.get_name())
print(persone_one.get_dob())

print(persone_one.set_dob('May  11, 2000'))
print(persone_one.get_dob())

# persone_one.dob = 'August 7, 1999'
# print(persone_one.__dob)
