# It's rare in the real world to see a class that defines properties the way we've been doing it:

class Soldier:
    name = "Legolas"
    armor = 2
    num_weapons = 2


# It's more practical to use a constructor. In Python, if you name a method __init__, that's the constructor and it is called when a new object is created.
# So, with a constructor, the code would look like this:

class Soldier:
    def __init__(self):
        self.name = "Legolas"
        self.armor = 2
        self.num_weapons = 2


# Now we can make the starting armor and number of weapons configurable with some parameters!

class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

soldier = Soldier("Legolas", 5, 10)
print(soldier.name)
# prints "Legolas"
print(soldier.armor)
# prints "5"
print(soldier.num_weapons)
# prints "10"


#multiple object

def main():
    aragorn = Brawler(4, 4, "Aragorn")
    gimli = Brawler(2, 7, "Gimli")
    legolas = Brawler(7, 7, "Legolas")
    frodo = Brawler(3, 2, "Frodo")

    fight(aragorn, gimli)
    fight(legolas, frodo)
    
# don't touch below this line


class Brawler:
    def __init__(self, speed, strength, name):
        self.speed = speed
        self.strength = strength
        self.power = speed * strength
        self.name = name


def fight(f1, f2):
    if f1.power > f2.power:
        print(f"{f1.name} wins with {f1.power} power over {f2.name}'s {f2.power}")
    elif f1.power < f2.power:
        print(f"{f2.name} wins with {f2.power} power over {f1.name}'s {f1.power}")
    else:
        print(f"It's a tie with both contestants at {f1.power} power")


main()