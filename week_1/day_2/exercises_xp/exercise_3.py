brand = {
    'name': 'Zara',
    'creation_date' : 1975,
    'creator_name' : 'Amancio Ortega Gaona' ,
    'type_of_clothes' : ['men', 'women', 'children', 'home' ],
    'international_competitors' : ['Gap', 'H&M', 'Benetton'],
    'number_stores' : 700,
    'major_color' : {
        'France': 'blue', 
        'Spain': 'red', 
        'US': 'pink ' 'green'
    }
}

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update({'number_stores': 2})
print("Zara clients are:")
for value in brand.get('type_of_clothes'):
    print(value, end=" / ")
brand.update({'country_creation' : 'Spain'})

for key in brand.keys():
    if key == 'international_competitors':
        print(f"\n{key} is in the dictionary brand")

brand.get('international_competitors').append('Desigual')

brand.pop('creation_date')
print(brand.get('international_competitors')[3])
print(brand['major_color']['US'])
print(brand)
i = 0
for key in brand.keys():
    i +=1
else:
    print(f"the number of keys is: {i}")

brand.update(more_on_zara)

print(brand.get('number_stores'))



