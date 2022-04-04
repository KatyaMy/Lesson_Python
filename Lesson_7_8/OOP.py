class Person:
    name = ""
    dod = ""

    def age(self):
        return "test age 20"

    def get_age(self):
        print(self.age())


person_1 = Person()
person_1.name = "John"
# person_1.dod = "03/28/2002"
# person_1.age = "20 years old"
person_1.get_age()