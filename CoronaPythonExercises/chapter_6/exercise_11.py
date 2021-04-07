cities = {
    'dublin': {
        'country': 'republic of ireland', 
        'population': '544.107',
        'fact': 'You can have a pint in a pub opened since 1198 AD, it is called the Brazen Head and is reputed to be the “Oldest Pub in Ireland”, located in Dublin.'
    },
    'amsterdam': {
        'country': 'Netherlands', 
        'population': '821.752',
        'fact': 'it’s possible to travel 100 kilometers (60 miles) on the water in the city limits.'
    },
    'london': {
        'country': 'England', 
        'population': '8.9 million',
        'fact': "Big Ben is arguably London’s most famous landmark. Surprisingly, it is actually meant to go by the name ‘The Clock Tower’, while ‘Big Ben’ is the name of the bell."
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {city_info['country'].title()}")
    print(f"Population: {city_info['population']}")
    print(f"Fun fact: {city_info['fact']}")