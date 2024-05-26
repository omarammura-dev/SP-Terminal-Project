class Cell:
    def __init__(self, id,region):
        self.id = id
        self.animals = []
        self.region = region 

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal_name):
        self.animals = [a for a in self.animals if a.name != animal_name]
