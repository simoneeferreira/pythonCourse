favorite_places = {
    'sarah':['rome','paris', 'london'],
    'josh': ['dublin', 'buenos aires', 'amsterdam'],
    'Adam':['portugal', 'los angeles', 'new york'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
           print(f"\t{place.title()}")