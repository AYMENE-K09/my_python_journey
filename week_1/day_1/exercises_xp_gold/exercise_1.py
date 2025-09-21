Spring = ['3', '4', '5']
Summer = ['6', '7', '8']
Autumn = ['9', '10', '11']
Winter = ['12', '1', '2']

active = True

while active:
    user_input = input("enter a random month: ")
    if user_input in Spring:
        print("We are in Spring now!!!")
        active = False
    
    elif user_input in Summer:
        print("We are in Summer now!!!")
        active = False

    elif user_input in Autumn:
        print("We are in Autumn now!!!")
        active = False

    if user_input in Winter:
        print("We are in Winter now!!!")
        active = False
    
    else:
        print("are you kidding me?")