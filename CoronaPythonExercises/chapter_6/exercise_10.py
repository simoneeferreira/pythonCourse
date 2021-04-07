favorite_number = {
   'jen': [2, 10],
    'sarah': [5, 15],
    'edward': [8, 11, 5],
    'phil': [13, 25], 
    'jonh': [1,8, 20],
}

for name, numbers in favorite_number.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")