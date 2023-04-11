class Dog:
    age_factor = 7
    def __init__(self, dog_age):
       self.human_age = Dog.age_factor * dog_age

doggy = Dog(6)
print(doggy.human_age)