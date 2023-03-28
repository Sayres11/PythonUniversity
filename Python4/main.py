# Zadanie 1
numbers_str = input("Podaj liczby oddzielone przecinkami: ")
numbers_list = numbers_str.split(",")

n = len(numbers_list)
for i in range(n):
    for j in range(n - 1):
        if numbers_list[j] > numbers_list[j + 1]:
            numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]

min_num = numbers_list[0]
max_num = numbers_list[-1]

print(f"Najmniejsza liczba: ", min_num)
print(f"Największa liczba: ", max_num)

# Zadanie 2

import random

cities_str = "Warszawa,Kraków,Wrocław,Łódź,Poznań,Gdańsk,Szczecin,Bydgoszcz,Lublin,Białystok"
cities_list = cities_str.split(",")

selected_cities = []
while len(selected_cities) < 10:
    city = random.choice(cities_list)
    if city not in selected_cities:
        selected_cities.append(city)

print("Wybrane miasta:")
for city in selected_cities:
    print(city)