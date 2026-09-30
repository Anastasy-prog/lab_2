import json

# Создаём словарь с данными
data = {
    "name": "Alex",
    "age": 20,
    "city": "Moscow",
    "skills": ["Python", "Java", "C++"]
}

# Сериализуем данные в JSON
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# Выводим результат
print(json_data)

# Сохраняем JSON в файл
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)