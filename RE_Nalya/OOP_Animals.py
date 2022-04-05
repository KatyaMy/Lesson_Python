class Alive:
    def __init__(self, eat, breath, reproduce):
        self.eat = eat
        self.breath = breath
        self.reproduce = reproduce

    #def animal(self):
    #print('Eats: ',self.eat, 'Breath:',self.breath,'Reproduce: ', self.reproduce)
    #
# tiger = Alive('Meet', 'lungs', 'mammal')
    #
# tiger.animal()

class Mammal(Alive):
    def __init__(self):
        super().__init__('milk', 'lungs', 'birth')

class Predator(Mammal):
    def __init__(self):
        super().__init__()
        self.feed = 'meat'
        self.feature = 'claws'


bobcat = Predator()

print(bobcat.feed)
print(bobcat.breath)

