class Person:
    def __init__(self, firstname, lastname, age, address, sex):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.address = address
        self.sex = sex

class Teacher(Person):
    def __init__(self, firstname, lastname, age, address, sex, salary, hours_per_week, speciality, degree):
        super().__init__(firstname, lastname, age, address, sex)
        self.salary = salary
        self.hours_per_week = hours_per_week
        self.speciality = speciality
        self.degree = degree

class Student(Person):
    def __init__(self, firstname, lastname, age, address, sex, class_n, mother_data, father_data, avarage_rez):
        super().__init__(firstname, lastname, age, address, sex)
        self.class_n = class_n
        self.mother_data = mother_data
        self.father_data = father_data
        self.avarage_rez = avarage_rez