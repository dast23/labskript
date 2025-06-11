text = input("Введите текст: ").split()
count = 0

for word in text:
    # Пропускаем пустые слова
    if not word:
        continue
        
    # Находим первую букву в слове
    for char in word:
        if char.isalpha():
            # Проверяем, начинается ли с "е" (учитываем оба регистра)
            if char.lower() == 'е':
                count += 1
            break  # Прерываем цикл после нахождения первой буквы

print(f"Количество слов, начинающихся с буквы 'е': {count}")