# exercise number 5

rivers = {
    'amazon': {
        'location': 'brazil',
        'length': '6,400 km',
    },
    'nile': {
        'location': 'egipt',
        'length': '6,650 km',
    },
    'mississippi': {
        'location': 'united states',
        'length': '3,730 km',
    },
}

for river, river_info in rivers.items():
    print(f"\nRiver: {river.title()}")
    print(f"Main location: {river_info['location'].title()}")
    print(f"Length: {river_info['length']}")