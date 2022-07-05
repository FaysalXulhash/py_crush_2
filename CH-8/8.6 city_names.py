def city_country(city, country):

    return f"{city.title()}, {country.title()}"


city = city_country('santiago', 'chile')
print(city)

city = city_country('dhaka', 'bangladesh')
print(city)

city = city_country('delhi', 'india')
print(city)
