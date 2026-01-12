"""
Phase 5: Object-Oriented Programming (OOP)
This script demonstrates how to structure code around objects, including inheritance,
encapsulation, and advanced class features.
"""
"""🧠 The Mental Model: Phase 5
OOP is about modeling your code after real-world objects. Instead of just writing a list of instructions (procedural programming), you create "things" that have properties and behaviors.

Classes vs. Objects (The Blueprint vs. The House):

Class: The architectural blueprint. It defines where the walls go and how the lights work. You can't live in a blueprint.
Object (Instance): The actual house built from that blueprint. You can build 50 identical houses (objects) from one blueprint (class).
__init__ & self (The Construction Crew & "Me"):

__init__: When you decide to build a house, this is the construction crew that shows up to set the initial state (paint color, number of rooms).
self: Imagine you are inside one specific house. When you say "turn on my lights" (self.lights), you mean the lights in this house, not the neighbor's house, even though they were built from the same blueprint.
Encapsulation (The Safe):

Some things in your house are for guests (Public: doorbell).
Some are for family only (Protected _: family_album).
Some are locked in a safe (Private __: social_security_card). You don't want outsiders messing with the wiring inside your walls directly; you give them a light switch (Getter/Setter) to interact with it safely.
Inheritance (Genetics):

A "Sports Car" is a child of "Car". It inherits wheels, an engine, and seats from "Car", but it adds a "Turbo" button and changes how the "Drive" method works. You don't have to reinvent the wheel.
Polymorphism (The Universal Remote):

You have a button labeled "Play". If you point it at a DVD player, it spins a disc. If you point it at a generic MP3 player, it plays a file. The interface ("Play") is the same, but the actual behavior differs depending on the object.
Magic Methods (The Wizardry):

Python objects are born knowing nothing. They don't know how to add themselves (+) or print themselves as text. Magic methods (like __add__ or __str__) teach them these fundamental skills."""
from abc import ABC, abstractmethod

def main():
    # ==========================================
    # 1. CLASSES & OBJECTS (The Blueprint & The House)
    # ==========================================
    print("--- 1. Classes & Objects ---")
    
    class Dog:
        # Class Variable: Shared by ALL instances of this class
        species = "Canis familiaris"

        # The Constructor: Initializes the object
        def __init__(self, name, age):
            # Instance Variables: Unique to EACH instance
            self.name = name
            self.age = age

        # Instance Method: Actions the object can perform
        def bark(self):
            return f"{self.name} says Woof!"

    # Instantiation: Creating objects from the class
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Rex", 5)

    print(f"{dog1.name} is a {dog1.species}")
    print(f"{dog2.name} is also a {dog2.species}")
    print(dog1.bark())

    # ==========================================
    # 2. INHERITANCE & POLYMORPHISM (Genetics & Overriding)
    # ==========================================
    print("\n--- 2. Inheritance & Polymorphism ---")
    
    # Single Inheritance: Cat inherits from Dog (just for example purposes!)
    class Cat(Dog):
        # Polymorphism: Method Overriding (Changing inherited behavior)
        def bark(self):
            return f"{self.name} says Meow!"

    cat = Cat("Whiskers", 2)
    # Inherits 'species' and '__init__' from Dog, but uses its own 'bark'
    print(f"{cat.name} (Species: {cat.species})") 
    print(cat.bark())

    # ==========================================
    # 3. ENCAPSULATION (Public, Protected, Private)
    # ==========================================
    print("\n--- 3. Encapsulation ---")
    
    class BankAccount:
        def __init__(self, owner, balance):
            self.owner = owner       # Public: Accessible from anywhere
            self._type = "Savings"   # Protected: Convention (don't touch outside class)
            self.__balance = balance # Private: Harder to access outside class

        def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                print(f"Deposited ${amount}")

        # Getter method to access private variable safely
        def get_balance(self):
            return self.__balance

    account = BankAccount("Alice", 1000)
    account.deposit(500)
    # print(account.__balance) # This would raise an AttributeError
    print(f"Balance: ${account.get_balance()}")

    # ==========================================
    # 4. ABSTRACTION (The Dashboard)
    # ==========================================
    print("\n--- 4. Abstraction ---")
    
    # Abstract Base Class: Cannot be instantiated, only inherited from
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius ** 2

    # shape = Shape() # Error: Cannot instantiate abstract class
    circle = Circle(5)
    print(f"Circle Area: {circle.area()}")

    # ==========================================
    # 5. DECORATORS (@classmethod, @staticmethod, @property)
    # ==========================================
    print("\n--- 5. Method Decorators & Properties ---")

    class Temperature:
        def __init__(self, celsius):
            self._celsius = celsius

        # @property: Access a method like an attribute (getter)
        @property
        def fahrenheit(self):
            return (self._celsius * 9/5) + 32

        # Setter for the property
        @fahrenheit.setter
        def fahrenheit(self, value):
            self._celsius = (value - 32) * 5/9

        # @classmethod: Works with the class, not the instance (Factory method)
        @classmethod
        def from_kelvin(cls, kelvin):
            return cls(kelvin - 273.15)

        # @staticmethod: Utility function, doesn't need self or cls
        @staticmethod
        def is_hot(celsius):
            return celsius > 30

    temp = Temperature(25)
    print(f"25C is {temp.fahrenheit}F (Calculated via property)")
    
    hot_day = Temperature.is_hot(35) # Static method call
    print(f"Is 35C hot? {hot_day}")

    # ==========================================
    # 6. MAGIC METHODS (Dunder Methods)
    # ==========================================
    print("\n--- 6. Magic Methods ---")
    
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        # __str__: Defines how the object looks as a string
        def __str__(self):
            return f"Vector({self.x}, {self.y})"

        # __add__: Defines behavior for the '+' operator
        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

    v1 = Vector(2, 4)
    v2 = Vector(1, 3)
    v3 = v1 + v2
    print(f"{v1} + {v2} = {v3}")

if __name__ == "__main__":
    main()