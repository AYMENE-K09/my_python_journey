
#-----------------------exercise_1-------------------------
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat_1 = Cat("mimi", 8)
cat_2 = Cat("momo", 4)
cat_3 = Cat("miami", 1)

def find_old_cat(Cat1, Cat2, Cat3):

    if Cat1.age > Cat2.age:
        if Cat1.age > Cat3.age:
            oldest_cat = Cat1
        else:
            oldest_cat = Cat3

    elif Cat2.age > Cat1.age:
        if Cat2.age > Cat3.age:
            oldest_cat = Cat2
        else:
            oldest_cat = Cat3

    print(f"The oldest cat is {oldest_cat.name} and it is {oldest_cat.age} years old")


find_old_cat(cat_1, cat_2, cat_3)

#-----------------------------------exercise_2------------------------------

class Dog:
    def __init__(self, name, height):
        self.dog_name = name
        self.dog_height = height

    def bark(self):
        print(f"{self.dog_name} goes woof!")

    def jump(self):
        print(f"{self.dog_name} jumps {self.dog_height * 2}cm")

davids_dog = Dog("Rex", 50)

sarahs_dog = Dog("Reacup", 20)

print(f"{davids_dog.dog_name}\n{davids_dog.dog_height}cm")

davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.dog_name}\n{sarahs_dog.dog_height}cm")

sarahs_dog.bark()
sarahs_dog.jump()


if sarahs_dog.dog_height > davids_dog.dog_height:
    print(f"{sarahs_dog.dog_name} is the bigger")

else:
    print(f"{davids_dog.dog_name} is the bigger")


#--------------------------------exercise_3--------------------------------

class Song:
    def __init__(self, lyrics = []):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()