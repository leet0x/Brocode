from math import *
class Person:
    '''this is a docstring. some description about our class'''

    def __init__(self, name, sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession

    #behavior (instance methods)
    def show(self):
        print("Name: ", self.name, "\nSex: ", self.sex, "\nProfession: ", self.profession)

    def work(self):
        print(self.name, "working as a", self.profession)

    def findMin(self, num1, num2, num3):
        min = num1

        if num2 < min:
            min = num2

        if num3 < min:
            min = num3

        return min


person = Person("Liku", "Male", "Software Developer")
person.show()
person.work()