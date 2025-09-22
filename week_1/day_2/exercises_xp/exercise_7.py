import random

def get_random_temp(season):
    seasons = ['WINTER', 'AUTUMN', 'SPRING', 'SUMMER']
    if season in seasons:
        print(f"we are in {season} season")
        if season == 'WINTER':
            return float(random.randint(-10, 16))
        elif season == 'AUTUMN':
            return float(random.randint(16, 23))
        elif season == 'SPRING':
            return float(random.randint(23, 32))
        elif season == 'SUMMER':
            return float(random.randint(32, 40))

def main():
    temp = get_random_temp(input("enter a season: ").upper())
   
    print(f"The temperature right now is {temp} degrees Celsius")
    if 0 > temp:
        print("Brr, that's freezing! Wear some extra layers tody")

    elif 0 < temp < 16:
        print("Quite chilly! Don't forget your coat")

    elif 16 < temp < 23:
        print("Drink hot tea before leaving")

    elif 24 < temp < 32:
        print("It is a nice day to walk")

    else:
        print("It is hot outside drik more water")

main()


