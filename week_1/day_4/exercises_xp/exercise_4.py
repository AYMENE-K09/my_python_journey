class Family():
    def __init__(self, last_name, members):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"congratulation!!! {kwargs['name']} into {self.last_name}'s family")

    def is_18(self, member_name):
            for member in self.members:
                if member['name'] == member_name:
                    if member['age'] >= 18:
                      return True
                    else:
                        return False
                
            return "member not found"
                 

    def family_presentation(self):
        print(f"Family :{self.last_name}")
        print("members:")
        for member in self.members:
            print(f" -{member['name']}, {member['age']} years old , {member['gender']}")

if __name__ == "__main__":
    my_family = Family("Spartacs", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
    ])
    my_family.born(name = 'Issam', age = 4, gender = 'Male', is_child = True)
    print(my_family.is_18('Issam'))
    my_family.family_presentation()