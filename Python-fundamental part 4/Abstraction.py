from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
class Lion(Animal):
    def make_sound(self):
       print("roar");
       
class Cow(Animal):
    def make_sound(self):
       print("wooo")
       
lion =Lion();

lion.make_sound()

#-----------------
# Import ABC (Abstract Base Class) and abstractmethod decorator
from abc import ABC, abstractmethod


# Abstract Class
# This class cannot be instantiated because it contains an abstract method.
class Animal(ABC):

    # Abstract Method
    # Every child class MUST implement this method.
    @abstractmethod
    def make_sound(self):
        pass


# Child Class 1
# Inherits from Animal
class Lion(Animal):

    # Implements the abstract method
    def make_sound(self):
        print("roar")


# Child Class 2
# Inherits from Animal
class Cow(Animal):

    # Implements the abstract method
    def make_sound(self):
        print("wooo")


# Creating an object of Lion
lion = Lion()

# Calling Lion's implementation of make_sound()
lion.make_sound()