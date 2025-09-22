# challenge 1

user_number = int(input("enter a number: "))
user_length = int(input("enter a lngth: "))
the_result = []

i = 1
while i <= user_length:
    calculation = user_number * i
    i += 1
    the_result.append(calculation)

print(the_result)

# challenge 2

user_input = input("enter a word like (mooooodaaaaillllll): ")
result = ""
last_char = ""

for char in user_input:
    if char != last_char:
        result += char
        last_char = char

print(result)