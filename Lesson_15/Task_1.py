class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print('Hello, my name is '+ self.firstname + ' ' + self.lastname + ' and I’m ' + str(self.age) + ' years old.')

pers = Person('Billy', 'Brown', 25)
pers.talk()
