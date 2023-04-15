class Animal:
    def __init__(self): pass

    def talk(self):
       raise NotImplementedError ('implemented be subclass')

class Cat(Animal):
    def talk(self):
        print('meow')

class Dog(Animal):
    def talk(self):
        print('woof woof')

def generic_function (animal):
   animal.talk()


kitty = Cat()
doggy = Dog()
generic_function(kitty)
generic_function(doggy)
