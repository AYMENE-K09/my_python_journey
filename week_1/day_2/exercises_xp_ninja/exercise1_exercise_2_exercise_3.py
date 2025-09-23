strings = "Volkswagen,Toyota,Ford Motor,Honda,Chevrolet"
my_list = strings.split(",")
my_list = sorted(my_list, reverse = True)
print("how many manufacturers/companies are in the list")
counter_o = 0
counter_i = 0
for word in my_list:
    for letter in word:
        if "o" in word:
            counter_o += 1
            break
        
        if "i" not in word:
            counter_i += 1
            break

print(f"{counter_o} nanufactures' names has letter 'o'")
print(f"{counter_i} nanufactures' names has letter 'i'")

my_list_2 = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

my_updated_list = set(my_list_2)
my_string = ", ".join(my_updated_list)
print(my_string)
print("how many comapanies are now in the list")

the_list = sorted(my_list)

reseversed_list_words = [word[::-1] for word in the_list]
print(reseversed_list_words)
    

#----------------------exercise_2--------------------

def get_full_name(first_name, middle_name, last_name):
    if not middle_name:
        middle_name = ""
        print(f"{first_name} {last_name}")

    else:
        print(f"{first_name} {middle_name} {last_name}")

first_name_user = input("enter your first name: ")
middle_name_user = input("enter your middle name: ")
last_name_user = input("enter your last name: ")
get_full_name(first_name_user, middle_name_user, last_name_user)


#--------------------exercise_3-------------------

Morse_dict = {
    'a' : ".-",'b' : "-...",'c' : "-.-.",'d' : "-..",'e' : ".",'f' : "..-.",'g' : "--.",'h' : "....",'i' : "..",'j' : ".---",'k' : "-.-",'l' : ".-..",'m' : "--",'n' : "-.",'o' : "---",'p' : ".--.",'q' : "--.-",'r' : ".-.",'s' : "...",'t' : "-",'u' : "..-",'v' : "...-",'w' : ".--",'x' : "-..-",'y' : "-.--",'z' : "--..", ' ' : "/"
}
print("Translate from English to Morse")
user_input = input("Enter text : ").lower()

user_list = list(user_input)
Morse_list = []
for letter in user_list:
    for key in Morse_dict:
        Morse_list.append(Morse_dict[letter])
        break
Morse_word = " ".join(Morse_list)
print(f"{user_input} >>> {Morse_word}")