from exercise_2 import Dog
import random

class PetDog(Dog):
    def __init__(self,name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
 
    def train(self):
        self.trained = True
        print(self.bark())

    def play(self, *dog_names):
        print(f"{dog_names} all play together")

    def do_a_trick(self):
        trick_1 = f"{self.name} does a barrel roll" 
        trick_2 = f"{self.name} stands on his back legs"
        trick_3 = f"{self.name} shakes your hand"
        trick_4 = f"{self.name} plays dead"
        trick_list = [trick_1, trick_2, trick_3, trick_4]
    
        if self.trained:
            print(random.choice(trick_list))
        
        else:
            print(f"{self.name} the dog is not trained")

doggie_1 = PetDog("sizar", 2, 2)
doggie_1.train()
doggie_1.play("x", "a", "y", "l")
doggie_1.do_a_trick()