import pickle
import os

def task1():
    """Работа со словарем студентов и файлом pickle"""
    # Создание словаря студентов
    students = {
        "Иванов": {"Математика": 4, "Физика": 5, "Химия": 3, "Биология": 4, "История": 5},
        "Петров": {"Математика": 3, "Физика": 4, "Химия": 5, "Биология": 3, "История": 4},
        "Сидоров": {"Математика": 5, "Физика": 5, "Химия": 5, "Биология": 5, "История": 5},
        "Козлова": {"Математика": 4, "Физика": 4, "Химия": 4, "Биология": 4, "История": 4},
        "Николаев": {"Математика": 3, "Физика": 3, "Химия": 3, "Биология": 3, "История": 3},
        "Федорова": {"Математика": 5, "Физика": 4, "Химия": 5, "Биология": 4, "История": 5},
        "Смирнов": {"Математика": 2, "Физика": 3, "Химия": 2, "Биология": 3, "История": 4}
    }
    
    print("\n" + "="*50)
    print("Список всех студентов и их баллов:")
    print("="*50)
    for student, grades in students.items():
        print(f"{student}: {', '.join([f'{subject}:{score}' for subject, score in grades.items()])}")
    
    # Расчет среднего балла для каждого студента
    print("\n" + "="*50)
    print("Средний балл каждого студента:")
    print("="*50)
    student_avg = {}
    for student, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        student_avg[student] = avg
        print(f"{student}: {avg:.2f}")
    
    # Поиск студентов с максимальным и минимальным средним баллом
    max_student = max(student_avg, key=student_avg.get)
    min_student = min(student_avg, key=student_avg.get)
    print("\n" + "="*50)
    print("Студенты с экстремальными средними баллами:")
    print("="*50)
    print(f"Максимальный средний балл: {max_student} ({student_avg[max_student]:.2f})")
    print(f"Минимальный средний балл: {min_student} ({student_avg[min_student]:.2f})")
    
    # Студенты с оценкой по математике выше средней
    math_scores = [grades["Математика"] for grades in students.values()]
    math_avg = sum(math_scores) / len(math_scores)
    print("\n" + "="*50)
    print(f"Средний балл по математике: {math_avg:.2f}")
    print("Студенты с оценкой по математике выше среднего:")
    print("="*50)
    for student, grades in students.items():
        if grades["Математика"] > math_avg:
            print(f"{student}: {grades['Математика']}")
    
    # Работа с файлом pickle
    print("\n" + "="*50)
    print("Работа с файлом pickle:")
    print("="*50)
    
    # Сохранение словаря в файл
    with open("data.pickle", "wb") as f:
        pickle.dump(students, f)
    print("Словарь сохранен в файл data.pickle")
    
    # Чтение словаря из файла
    with open("data.pickle", "rb") as f:
        loaded_students = pickle.load(f)
    print("\nСловарь успешно загружен из файла data.pickle")
    print(f"Проверка: первый студент в загруженном словаре - {list(loaded_students.keys())[0]}")

def task2():
    """Подсчет слов в каждой строке текстового файла"""
    print("\n" + "="*50)
    print("Подсчет слов в каждой строке файла:")
    print("="*50)
    
    # Создаем тестовый файл, если его нет
    if not os.path.exists("input.txt"):
        with open("input.txt", "w", encoding="utf-8") as f:
            f.write("Это первая строка файла\n")
            f.write("А это вторая строка, в ней больше слов\n")
            f.write("Третья строка!\n")
            f.write("И последняя четвертая строка текста")
        print("Создан тестовый файл input.txt")
    
    # Чтение файла и подсчет слов
    word_counts = []
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            word_counts.append(len(line.split()))
    
    # Запись результатов в файл
    with open("output.txt", "w", encoding="utf-8") as f:
        for i, count in enumerate(word_counts, 1):
            f.write(f"Строка {i}: {count} слов(а)\n")
    
    print("\nРезультат подсчета слов по строкам:")
    for i, count in enumerate(word_counts, 1):
        print(f"Строка {i}: {count} слов(а)")
    print("\nРезультат записан в файл output.txt")

def main():
    """Главное меню программы"""
    while True:
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*50)
        print("1. Работа со словарем студентов")
        print("2. Подсчет слов в текстовом файле")
        print("0. Выход")
        
        choice = input("Выберите задачу (0-2): ")
        
        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '0':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()