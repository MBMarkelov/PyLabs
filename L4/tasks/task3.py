def map_cities(city_names):
    return [city if len(city) > 5 else '-' for city in city_names.split()]


'''
cities = input("Введите названия городов через пробел: ")
result = map_cities(cities)
print(result)
'''
