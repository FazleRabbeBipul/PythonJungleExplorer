# Abstraction helps us handle complexity by hiding unnecessary details. 
# Sounds like encapsulation, right? They're so similar that it's almost not worth worrying about the difference...almost.

# ****** Abstraction vs encapsulation *******
# Abstraction is about creating a simple interface for complex behavior. It focuses on what's exposed.
# Encapsulation is about hiding internal state. It focuses on tucking implementation details away so no one depends on them.
# Abstraction is more about reducing complexity, encapsulation is more about maintaining the integrity of system internals.

import random
attack_damage = random.randrange(5)

# Generating random numbers is a really hard problem. The operating system uses the physical hardware of the computer to create a seed for the randomness. 

# However, the developers of the random library have abstracted that complexity away 
# and encapsulated it within the simple randrange function. 

# We just say "I want a random number from 0 to 4" and the library does it.
# When writing libraries for use by other developers, getting the abstractions right is crucial because changing them later can be disastrous. 
# Imagine if the maintainers of the random module changed the input parameters to the randrange function! It would break code all over the world.


# Abstraction is about reducing complexity. Creating good abstractions is particularly crucial when you're developing libraries
#  for other developers to use. For example, the built-in pow function in Python is an abstraction that hides the complexity of calculating exponents.

# # pow isn't magic. Somewhere, code that does something like this exists and is called when you use pow:

def pow(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


import math

class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__result += a

    def subtract(self, a):
        self.__result -= a

    def multiply(self, a):
        self.__result *= a

    def divide(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result /= a
            

    def modulo(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result %= a

    def power(self, a):
        self.__result **= a

    def square_root(self):
        self.__result = math.sqrt(self.__result)
        

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result
