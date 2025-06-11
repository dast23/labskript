import requests
import json
import os
import csv
from bs4 import BeautifulSoup
from time import sleep

def part1_countries():
    print("Запуск Части 1: Получение данных о странах...")
    # Получение данных об азиатских странах
    url = "https://restcountries.com/v3.1/region/asia"
    try:
        response = requests.get(url)
        response.raise_for_status()
        countries = response.json()
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return
    
    # Фильтрация и обработка данных
    filtered_countries = []
    for country in countries:
        try:
            population = country.get('population', 0)
            if population > 30_000_000:
                name = country['name']['common']
                capital = country.get('capital', ['N/A'])[0]
                area = country.get('area', 0)
                cca2 = country.get('cca2', '').lower()
                
                # Проверка наличия необходимых данных
                if not area or not cca2:
                    continue
                    
                density = population / area
                
                filtered_countries.append({
                    'name': name,
                    'capital': capital,
                    'area': area,
                    'population': population,
                    'density': density,
                    'cca2': cca2
                })
        except KeyError as e:
            print(f"Пропуск страны из-за ошибки: {e}")
            continue
    
    # Сохранение данных в JSON
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(filtered_countries, f, ensure_ascii=False, indent=4)
    
    # Топ-5 стран по плотности населения
    filtered_countries.sort(key=lambda x: x['density'], reverse=True)
    top_5 = filtered_countries[:5]
    
    print("\nТоп-5 стран по плотности населения:")
    for i, country in enumerate(top_5, 1):
        print(f"{i}. {country['name']} - {country['density']:.2f} чел/км²")
    
    # Скачивание флагов
    os.makedirs('flags', exist_ok=True)
    for country in top_5:
        name = country['name']
        flag_url = f"https://flagcdn.com/w320/{country['cca2']}.png"
        try:
            flag_data = requests.get(flag_url).content
            with open(f'flags/{name}.png', 'wb') as f:
                f.write(flag_data)
            print(f"Флаг {name} сохранен в flags/{name}.png")
        except Exception as e:
            print(f"Ошибка при загрузке флага {name}: {e}")
    
    print("Часть 1 завершена. Данные сохранены в results.json и флаги в папке flags\n")

def part2_athletics():
    print("Запуск Части 2: Сбор данных о спортивных рекордах...")
    # Конфигурация параметров
    years = range(2001, 2025)
    genders = ['men', 'women']
    events = {
        '60m': ('60-metres', 'indoor'),
        '100m': ('100-metres', 'outdoor'),
        '200m': ('200-metres', 'outdoor'),
        '400m': ('400-metres', 'outdoor')
    }
    
    # Подготовка CSV файла
    with open('top_results.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Year', 'Event', 'Gender', 'Athlete', 'Country', 'Result', 'Date'])
    
    total_requests = len(years) * len(genders) * len(events)
    processed = 0
    
    # Сбор данных
    for year in years:
        for gender in genders:
            for event_name, (event_slug, venue) in events.items():
                processed += 1
                print(f"Обработка: {year} {gender} {event_name} ({processed}/{total_requests})")
                
                url = (
                    f"https://worldathletics.org/records/toplists/sprints/"
                    f"{event_slug}/{venue}/{gender}/senior/{year}"
                )
                
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Поиск таблицы результатов
                    table = soup.find('table', class_='records-table')
                    if not table:
                        print(f"  Таблица не найдена: {url}")
                        continue
                    
                    # Поиск строк с результатами
                    rows = table.find('tbody').find_all('tr', limit=1)
                    if not rows:
                        print(f"  Нет данных в таблице: {url}")
                        continue
                    
                    # Обработка первой строки (топ-1)
                    row = rows[0]
                    cells = row.find_all('td')
                    
                    # Извлечение данных из ячеек
                    result = cells[3].get_text(strip=True)
                    athlete_tag = cells[4].find('a')
                    athlete = athlete_tag.get_text(strip=True) if athlete_tag else "N/A"
                    
                    country_tag = cells[4].find('span')
                    country = country_tag.get_text(strip=True) if country_tag else "N/A"
                    
                    date = cells[8].get_text(strip=True) if len(cells) > 8 else "N/A"
                    
                    # Сохранение в CSV
                    with open('top_results.csv', 'a', encoding='utf-8', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow([
                            year, event_name, gender, 
                            athlete, country, result, date
                        ])
                    
                    # Пауза для снижения нагрузки на сервер
                    sleep(0.5)
                    
                except Exception as e:
                    print(f"  Ошибка при обработке URL {url}: {e}")
    
    print("\nЧасть 2 завершена. Данные сохранены в top_results.csv")

if __name__ == "__main__":
    # Выполнение Части 1
    part1_countries()
    
    # Выполнение Части 2
    part2_athletics()
    
    print("\nОбе задачи успешно выполнены!")
    print("Результаты Части 1: results.json и папка flags")
    print("Результаты Части 2: top_results.csv")