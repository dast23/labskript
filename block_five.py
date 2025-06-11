import math

def calculate_area():
    """Вычисление площади геометрических фигур"""
    print("\n" + "="*50)
    print("Вычисление площади геометрических фигур")
    print("="*50)
    print("1. Прямоугольник")
    print("2. Треугольник")
    print("3. Круг")
    print("4. Трапеция")
    print("5. Параллелограмм")
    print("0. Вернуться в главное меню")
    
    choice = input("Выберите фигуру (0-5): ")
    
    if choice == '1':
        # Прямоугольник
        a = float(input("Введите длину: "))
        b = float(input("Введите ширину: "))
        area = a * b
        print(f"Площадь прямоугольника: {area:.2f}")
        
    elif choice == '2':
        # Треугольник
        a = float(input("Введите основание: "))
        h = float(input("Введите высоту: "))
        area = 0.5 * a * h
        print(f"Площадь треугольника: {area:.2f}")
        
    elif choice == '3':
        # Круг
        r = float(input("Введите радиус: "))
        area = math.pi * r ** 2
        print(f"Площадь круга: {area:.2f}")
        
    elif choice == '4':
        # Трапеция
        a = float(input("Введите верхнее основание: "))
        b = float(input("Введите нижнее основание: "))
        h = float(input("Введите высоту: "))
        area = 0.5 * (a + b) * h
        print(f"Площадь трапеции: {area:.2f}")
        
    elif choice == '5':
        # Параллелограмм
        a = float(input("Введите основание: "))
        h = float(input("Введите высоту: "))
        area = a * h
        print(f"Площадь параллелограмма: {area:.2f}")
        
    elif choice == '0':
        return
    
    else:
        print("Неверный выбор!")
    
    calculate_area()  # Показать меню снова

def count_digits(n):
    """Рекурсивная функция подсчета цифр в числе"""
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

# Главное меню программы
while True:
    print("\n" + "="*50)
    print("ГЛАВНОЕ МЕНЮ")
    print("="*50)
    print("1. Вычисление площади геометрических фигур")
    print("2. Подсчет количества цифр в числе")
    print("0. Выход")
    
    choice = input("Выберите действие (0-2): ")
    
    if choice == '1':
        calculate_area()
        
    elif choice == '2':
        print("\nПодсчет количества цифр в числе")
        try:
            num = int(input("Введите натуральное число: "))
            if num < 0:
                print("Число должно быть натуральным (положительным)!")
            else:
                digits = count_digits(num)
                print(f"Количество цифр в числе {num}: {digits}")
        except ValueError:
            print("Ошибка! Введите целое число.")
            
    elif choice == '0':
        print("Программа завершена.")
        break
        
    else:
        print("Неверный выбор! Попробуйте снова.")