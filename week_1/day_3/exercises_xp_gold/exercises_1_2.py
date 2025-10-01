#----------------------exercise_1--------------------

import math

class Circle():
    def __init__(self, radius = 1.0):
        self.radius = radius

    def method_1(self):
        return  round(2 * math.pi * self.radius , 2)

    def method_2(self):
        return round(math.pi * pow(self.radius, 2), 2)

    def geomet_of_circe(self):
        print("A circle is the set of all points in a plane that are equidistant from a fixed point called the center. The constant distance is the radius.")

my_circle = Circle()
print(my_circle.method_1())
print(my_circle.method_2())
my_circle.geomet_of_circe()

#-------------------------exercise_2-------------------

class MyList():
    def __init__(self, mylist):
        self.mylist = mylist

    def reversed_list(self):
        return sorted(self.mylist, reverse = True)
    
    def sorted_list(self):
        return self.mylist
    
    def number_list(self):
        i = 0
        my_number_list = []
        for i in range(len(self.mylist)):
            my_number_list.append(i)
        
        print(my_number_list)
    
ob_1 = MyList(['a', 'b', 'c', 'd', 'e', 'f'])
print(ob_1.reversed_list())
print(ob_1.sorted_list())
ob_1.number_list()

