class Dog():
    def __init__(self,name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
    
    def run_speed(self):
        return self.weight / self.age * 10


    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} won the fight"
        
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f"{other_dog.name} won the fight"
        
        else:
            return f"it is a tie between {self.name} and {other_dog.name}"
    
if __name__ == "__main__":
    dog_1 = Dog("Spike", 4, 18)
    dog_2 = Dog("Sizar", 2, 17)
    dog_3 = Dog("Bogi", 3, 15)
    other_dog = Dog("Victor", 2, 16)

    Dogs = [dog_1, dog_2, dog_3]

    for dog in Dogs:
        print(dog.bark())
        dog.run_speed()
        print(dog.fight(other_dog))