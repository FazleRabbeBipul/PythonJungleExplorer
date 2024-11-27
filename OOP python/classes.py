
# Chapter 01
# "Classes" are custom new types that we define as the programmer. Each new instance of a class is an "object".

# Assignment
# Create a class called Wall. It should have a property called armor that is initialized to 10 and a height that starts at 5.

class Wall:
    armor = 10
    height = 5


# One thing that makes classes cool is that we can define methods on them. A method is a function that's tied directly to a class and has access to all its properties.
# Self : Methods are nested within the class declaration. Their first parameter is always the instance of the class that the method is being called on. 
# By convention, it's called "self". Because self is a reference to the object, you can use it to read and update the properties of the object.

# Notice that methods are called directly on an object using the dot operator.
#  my_object.my_method()


# Add a fortify() method to your wall class. It should double the current armor property.

class Wall:
    armor = 10
    height = 5

    def fortify(self):
        self.armor *= 2


# In contrast, methods often don't return anything explicitly because they can mutate the properties of the object instead. That's exactly what we did in the last assignment.
# However, they can return values if you want! They're just functions with access to an object, after all.

class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        cost = self.armor * self.height
        return cost

    # don't touch below this line

    def fortify(self):
        self.armor *= 2
