user_number = int(input("enter a number: "))
user_length = int(input("enter a lngth: "))
the_result = []

i = 1
while i <= user_length:
    calculation = user_number * i
    i += 1
    the_result.append(calculation)

print(the_result)