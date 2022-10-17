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

    def printString(self, someString):
        for character in someString:
            print(character, end="  ")
            # print(character)

    def findMinList(self, list):
        min = list[0]
        for item in list:
            if item < min:
                min = item

        return min

    def printRange(self):
        for counter in range(10):
            print(counter)


person = Person("Liku", "Male", "Software Developer")
# person.show()
# person.work()
# person.printString(person.profession)
# list = [5, 6, 3, 8, 9, 4]
# print(person.findMinList(list))
person.printRange()