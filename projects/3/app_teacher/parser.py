import requests
import json
import time

# params = {
#     'text': 'NAME:Аналитик',  # Текст фильтра. В имени должно быть слово "Аналитик"
#     'area': 1,  # Поиск ощуществляется по вакансиям города Москва
#     'page': 1,  # Индекс страницы поиска на HH
#     'per_page': 100  # Кол-во вакансий на 1 странице
# }

# req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API

vacancy_id = 55508596
url = f'https://api.hh.ru/vacancies/{vacancy_id}'
response = requests.get(url=url)

if response.status_code != 200 and False:
    print("Ошибка: " + str(response.status_code))
else:
    print(response.content)
    data = response.content.decode()

    with open("vacancy.json", "w", encoding='utf8') as file:
        file.write(json.dumps(data, ensure_ascii=False))

    # data
    json_data = json.loads(response.content)
    print(json_data)
    print(type(json_data))
    description = json_data["description"]
    print(description)
    arr = description.split('<strong>')
    arr = arr[-1]
    arr = arr.split('</strong></p>')[0]
    print(arr)

    # ['1', '2', '3']
    # string_find = arr[-1] # [старт:стоп:шаг]
    # print(string_find)
    #
    # description = 'description'
    # print(description[::2])

vacancies = []

for i in range(0, 5):
    time.sleep(0.0001)
    params = {
        'text': 'NAME:Программист',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': 40,  # Поиск ощуществляется по вакансиям города Москва
        'page': i,  # Индекс страницы поиска на HH
        'per_page': 100  # Кол-во вакансий на 1 странице
    }
    response = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
    json_data1 = json.loads(response.content.decode())
    # print(json_data1)
    print("len items:", len(json_data1["items"]))
    for j in json_data1["items"]:
        vacancies.append(j)

print(vacancies)
print(len(vacancies))
for i in vacancies:
    # print(i)
    try:
        description = i["name"]
        print()
        arr = description.split('<strong>')[-1].split('</strong></p>')[0]
        print("published_at: ", i["published_at"].split('T')[0], "id: " + i["id"], "name: ", arr)
    except Exception as error:
        print(error)

    print(i["published_at"].split('T'))
