class Zoo:
    def __init__ (self, zoo_name):
        self.animals = []
        self.name_of_the_zoo = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            print(f"'{new_animal}' added in the {self.name_of_the_zoo}")
            self.animals.append(new_animal)
        
        else:
            print(f"'{new_animal}' is already in {self.name_of_the_zoo}")
    
    def get_animals(self):
        print(self.animals)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            print(f"{animal_sold} has sold")
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} is not in {self.name_of_the_zoo}")

    def sort_animals(self):
        self.animals.sort()
        self.group = {}
        for animal in self.animals:
            animal_first_letter = animal[0]
            if animal_first_letter not in self.group:
                self.group[animal_first_letter] = animal
            else:
                self.group[animal_first_letter] = [animal]
                self.group[animal_first_letter].append(animal)
    def get_groups(self):
        print(self.group)

new_york_zoo = Zoo("new_york_zoo")

animals = ["Bear", "Ape", "Cougar", "Baboon", "Eel", "Cat", "Emu"]
for animal in animals:
    new_york_zoo.add_animal(animal)

new_york_zoo.get_animals()
new_york_zoo.sell_animal(input("enter the animal you wanna sell: "))
new_york_zoo.sort_animals()
new_york_zoo.get_groups()