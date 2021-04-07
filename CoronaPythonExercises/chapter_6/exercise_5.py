rivers = {
    'amazon': 'brazil',
    'nile': 'egipt',
    'mississippi': 'united states',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.\n")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())