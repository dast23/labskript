import os
import glob
import subprocess
import platform

def clear_screen():
    """Очистка экрана консоли"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def print_menu():
    """Вывод меню"""
    print("\n" + "=" * 50)
    print("КОНСОЛЬНЫЙ ФАЙЛОВЫЙ МЕНЕДЖЕР")
    print("=" * 50)
    print("1. Открыть файл в текстовом редакторе")
    print("2. Показать содержимое файла")
    print("3. Найти файлы по имени")
    print("4. Показать содержимое директории")
    print("0. Выход")
    print("=" * 50)

def open_file_in_editor():
    """Открытие файла в текстовом редакторе"""
    file_path = input("Введите путь к файлу: ")
    
    if not os.path.exists(file_path):
        print("Файл не существует!")
        return
    
    if not os.path.isfile(file_path):
        print("Указанный путь не является файлом!")
        return
    
    # Выбор редактора в зависимости от ОС
    if platform.system() == "Windows":
        try:
            # Пробуем открыть в Notepad++
            subprocess.run(['notepad++', file_path])
        except FileNotFoundError:
            # Если не установлен Notepad++, используем стандартный блокнот
            os.startfile(file_path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(['open', '-t', file_path])
    else:  # Linux и другие UNIX-подобные
        subprocess.run(['xdg-open', file_path])
    
    print(f"Файл {file_path} открыт в текстовом редакторе")

def show_file_content():
    """Вывод содержимого файла"""
    file_path = input("Введите путь к файлу: ")
    
    if not os.path.exists(file_path):
        print("Файл не существует!")
        return
    
    if not os.path.isfile(file_path):
        print("Указанный путь не является файлом!")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("\n" + "=" * 50)
            print(f"Содержимое файла {file_path}:")
            print("=" * 50)
            print(content)
    except UnicodeDecodeError:
        print("Не удалось прочитать файл (возможно, это бинарный файл)")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

def find_files():
    """Поиск файлов по шаблону"""
    pattern = input("Введите имя файла или шаблон для поиска: ")
    
    # Поиск файлов с использованием glob (рекурсивно)
    found_files = glob.glob(f"**/{pattern}", recursive=True)
    
    if not found_files:
        print("Файлы не найдены!")
        return
    
    print("\nНайденные файлы:")
    for i, file_path in enumerate(found_files, 1):
        print(f"{i}. {os.path.abspath(file_path)}")

def list_directory_contents():
    """Вывод содержимого директории"""
    dir_path = input("Введите путь к директории (оставьте пустым для текущей): ").strip()
    
    if not dir_path:
        dir_path = os.getcwd()
    
    if not os.path.exists(dir_path):
        print("Директория не существует!")
        return
    
    if not os.path.isdir(dir_path):
        print("Указанный путь не является директорией!")
        return
    
    print(f"\nСодержимое директории {os.path.abspath(dir_path)}:")
    print("=" * 50)
    
    # Получаем список элементов директории
    items = os.listdir(dir_path)
    
    # Разделяем файлы и директории
    directories = []
    files = []
    
    for item in items:
        full_path = os.path.join(dir_path, item)
        if os.path.isdir(full_path):
            directories.append(f"[DIR] {item}")
        else:
            files.append(f"[FILE] {item}")
    
    # Выводим сначала директории, потом файлы
    for item in sorted(directories):
        print(item)
    
    for item in sorted(files):
        print(item)
    
    print("\nВсего элементов:", len(items))

def main():
    """Главная функция файлового менеджера"""
    while True:
        clear_screen()
        print_menu()
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            open_file_in_editor()
        elif choice == '2':
            show_file_content()
        elif choice == '3':
            find_files()
        elif choice == '4':
            list_directory_contents()
        elif choice == '0':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()