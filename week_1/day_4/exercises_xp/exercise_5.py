from exercise_4 import Family

class TheIncredibles(Family):

    def use_power(self):
        for member in self.members:
            if member['age'] > 18:
                print(f"{member['name']}'s power is {member['power']}")

            else:
                print(f"{member['name']} has no power yet")

    def incredible_presentation(self):
        print("HERE IS OUR POWERFUL FAMILY:")
        super().family_presentation()
        print("OUR POWERS:")
        for member in self.members:
            print(f" -{member['incredible_name']} can {member['power']} ")

our_incredible_family = TheIncredibles( "The vicotorios",[
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ])

our_incredible_family.incredible_presentation()
our_incredible_family.born(name = 'Jack', age = 4, gender = 'Male', is_child = True, power = 'Unkown', incredible_name = 'Baby Jack')
our_incredible_family.use_power()
our_incredible_family.incredible_presentation()