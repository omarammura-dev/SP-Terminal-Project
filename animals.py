"""
Ömer Ammura - 234210074
Emad CheikhElichreh - 224210087
Mohammad nikpour -  234210005
Eldar Semnov - 224210122
"""


class Animal:
    def __init__(self, name, species, age, health, gender,abilities=None):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
        self.gender = gender
        self.abilities = abilities

class Predator(Animal):
    def __init__(self, name, age, health, gender,abilities=None):
        super().__init__(name, "vahşi", age, health, gender,abilities)

class Bird(Animal):
    def __init__(self, name, age, health, gender,abilities=None):
        super().__init__(name, "Kuş", age, health, gender,abilities)

class Herbivore(Animal):
    def __init__(self, name, age, health, gender,abilities=None):
        super().__init__(name, "Otobur", age, health, gender,abilities)
