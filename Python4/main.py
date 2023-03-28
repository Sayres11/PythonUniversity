numbers_str = input("Podaj liczby oddzielone przecinkami: ")
numbers_list = numbers_str.split(",")

n = len(numbers_list)
for i in range(n):
    for j in range(n - 1):
        if numbers_list[j] > numbers_list[j + 1]:
            numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]

min_num = numbers_list[0]
max_num = numbers_list[-1]

print(f"Najmniejsza liczba: ",  min_num)
print(f"Największa liczba: ", max_num)
