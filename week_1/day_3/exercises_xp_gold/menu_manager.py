
class MenuManger():
    def __init__(self):
        self.menu = [{'name': 'Soup','price': 10,'spice_level': 'B','gluten': False},{'name': 'Hamburger','price': 15,'spice_level': 'A','gluten': True},{'name': 'Salad','price': 18,'spice_level': 'A','gluten': False},{'name': 'French Fries','price': 5,'spice_level': 'C','gluten': False},{'name': 'Beef bourguignon','price': 25,'spice_level': 'B','gluten': True}]

    def add_item(self , name, price, spice_level, gluten):
        dict_added = {'name' : name, 'price' : price, 'spice_level' : spice_level, 'gluten' : gluten}
        if dict_added in self.menu:
            print("this dish is already exist.")

        elif dict_added not in self.menu:
                    self.menu.append(dict_added)
                    print(f"{name} dish is added")

    def update_item(self, name, price, spice_level, gluten):
        dict_update = {'name' : name, 'price' : price, 'spice_level' : spice_level, 'gluten' : gluten}
        if dict_update in self.menu:
            print(f"{name} dish is updated")

        else:
            print(f"{name} dish is not exist")     
         
    def remove_item(self, name):
        for dict in self.menu:
            if dict['name'] == name:
                self.menu.remove(dict)
                return f"{name} was removed from the menu"
            
        return f"{name} is not in the menu"
        
    def show_menu(self):
        print("--------------------")
        print("Today Menu")
        print("--------------------")
        for dict in self.menu:
            print(*dict.values())     

restaurant = MenuManger()
restaurant.add_item("Rice", 18, "C", False)
restaurant.update_item("Hamburger", 15, "A", True)
print(restaurant.remove_item("Salad"))
restaurant.show_menu()