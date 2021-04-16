def city_country(city_name, country_name):
    full_text = f"{city_name.title()}, {country_name.title()}."
    return full_text

# print(city_country('santiago', 'chile'))

city = city_country('santiago', 'chile')
print(city)

city = city_country('sao paulo', 'brazil')
print(city)

city = city_country('dublin', 'ireland')
print(city)