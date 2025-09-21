user_input = input("enter a word like (mooooodaaaaillllll): ")
result = ""
last_char = ""

for char in user_input:
    if char != last_char:
        result += char
        last_char = char

print(result)