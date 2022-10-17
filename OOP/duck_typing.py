# Duck typinh = concept where the class of an object is less important than the methods
# class type is not checked if minimum methods/attributes are present
# "If it walks like a duck, and it quacks like a duck, then it must be a duck

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def talk(self):
        pass


class Duck(Animal):
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")


class Chicken(Animal):
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")


class Person(Animal, ABC):
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter.")
        
        
duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)