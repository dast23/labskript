a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

# Проверка попадания в интервал [1, 3]
result = []

for number in (a, b, c):
    if 1 <= number <= 3:
        result.append(number)

# Вывод результата
print("Числа в интервале [1, 3]:", result)