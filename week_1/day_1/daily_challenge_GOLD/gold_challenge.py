print("enter your birthday DD/MM/YYYY ")
Day = int(input("day: "))
Month = int(input("month: "))
Year = int(input("year: "))

user_age = 2025 - Year
print(f"You were born in {Day}/{Month}/{Year} and you are {user_age} years old")

str_age = list(str(user_age))
int_age = int(str_age[1])
user_candles_numbers = int_age * "i"
print("    ___",user_candles_numbers,"___")
print("   |:H:a:p:p:y:|")
print(" __|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")