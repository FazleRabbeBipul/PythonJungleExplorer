# Encapsulation
# Encapsulation is the practice of hiding complexity inside a "black box" so that it's easier to focus on the problem at hand.
# The most basic example of encapsulation is a function. The caller of a function doesn't need to worry too much about what happens inside, 
# they just need to understand the inputs and outputs.

# acceleration = calc_acceleration(initial_speed, final_speed, time)
# To use the calc_acceleration function, we don't need to think about every individual line of code inside the function. We just need to know that if we give it the inputs:
# initial_speed
# final_speed
# time
# Then it will give us the correct acceleration as an output.

# By default, all properties and methods in a class are public. That means that you can access them with the . operator:

# wall.height = 10
# print(wall.height)
# # 10


# Private data members are how we encapsulate logic and data within a class. 
# To make a property or method private, you just need to prefix it with two underscores.

class Wall:
    def __init__(self, armor, magic_resistance):
        self.__armor = armor
        self.__magic_resistance = magic_resistance

    def get_defense(self):
        return self.__armor + self.__magic_resistance

front_wall = Wall(10, 20)

# This results in an error
print(front_wall.__armor)

# This works
print(front_wall.get_defense())
# 30


# We do this because, in this example, armor and magic_resistance are implementation details. 
# After creating a Wall, they don't matter anymore. Now the game developers can just call get_defense and not worry about how it's calculated under the hood.



class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if(amount <= 0):
            raise ValueError("Cannot deposit zero or negative funds")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if(amount <= 0):
            raise ValueError("Cannot withdraw zero or negative funds")
        elif(amount > self.__balance):
            raise ValueError("Insufficient funds")
        else:
            self.__balance -= amount
