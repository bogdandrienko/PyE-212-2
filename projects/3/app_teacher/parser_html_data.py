import requests
from bs4 import BeautifulSoup

url = f'https://myfin.by/converter.html'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
response = requests.get(url=url, headers=headers)  # http запрос

soup = BeautifulSoup(response.content, 'html.parser')
data1 = soup.find_all('span', itemprop="text")


print()




# локальное сохранение HTML
with open(file='new.html', mode='w', encoding="utf-8") as file:
    file.write(response.content.decode())
print('1 \n\n\n\n\n')

html_data = response.content.decode()
print(html_data)
print(type(html_data))

print('2 \n\n\n\n\n')

#  0  1
# [A, B]

str1 = 'converter-container converter-container-in-grid'
small_html1 = html_data.split(str1)[-1]  # обрезаем верх ненужных данных и берём последнюю таблицу

str2 = '<a href="'
small_html1 = small_html1.split(str2)[0]  # обрезаем низ ненужных данных

print(small_html1)
print(len(small_html1))

print('3 \n\n\n\n\n')

str3 = 'class="converter-container__item-input-wrapper"'
str4 = 'type="tel"'

# small_html2 = small_html1.split(str3)[-1].split('value="')[-1].split('"')[0]
small_html2 = small_html1.split(sep=str3)  # возвращает массив разделенных объектов по сепаратору

# print(small_html2)

all_list = []
for value in small_html2[1::1]:
    print(value + '\n\n')

    separator1 = 'class="converter-container__item-currency-name">'
    name1 = value.split(separator1)  # разделили предыдущую строку по сепаратору на 2 части
    print(name1)
    name2 = name1[1]  # взяли только вторую часть (нижнюю)
    print(name2)
    separator2 = '</div>'
    name3 = name2.split(separator2)  # разделили предыдущую строку по сепаратору на 2 части
    print(name2)
    name4 = name3[0]  # взяли только первую часть (верхнюю)
    print(name4)
    name5 = name4.strip()  # очистили пробелы и отступы по краям
    print(name5)

    value1 = value.split('value="')[1].split('"/>')[0]

    abbr1 = value.split('<span class="converter-container__item-currency-abbr">')[1].split('<')[0]

    print(f'валюта: {name5}, значение: {value1}, аббреиватура: {abbr1}')
    # all_list.append((value1, name5, abbr1))
    # all_list.append([value1, name5, abbr1])
    all_list.append({"значение": value1, "валюта": name5, "аббреиватура": abbr1})
    # all_list.append(i.split('"')[0])

    # print(value.split('</div>')[0].strip())

print(all_list)
for i in all_list:
    print(type(i))
    print(f'валюта: {i["валюта"]}, значение: {i["значение"]}')

print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')
print('3 \n\n\n\n\n')

print(all_list)

print('4 \n\n\n\n\n')

# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)


word = 'Banana, Apple, Kiwi'
print(word)
print(word.split(', '))
print(type(word.split(', ')))

str1 = """
<div class="converter-container__item-input-wrapper">
    <span class="converter-container__item-currency-abbr">
        uah
    </span>
    <input type="tel" inputmode="decimal" id="bestb_uah" class="input_calc form-control form-input-sum bestb" value="84.9026">
    <span class="converter-container__item-delete" data-js="hide-item" data-del="bestbuah" style="display: none"></span>
</div>
"""

print('5 \n\n\n\n\n')

str6 = str1.split('<span class="converter-container__item-currency-abbr">')[1]
#
print(str6)
print(type(str6))

print('6 \n\n\n\n\n')

str7 = str6.split('</span>')[0].strip()
print(str7)
print(type(str7))



# url = f'https://www.google.com/search?q=google+%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&rlz=1C1IXYC_ruKZ978KZ978&oq=google+%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&aqs=chrome..69i57j0i457i512j0i512l8.7400j1j7&sourceid=chrome&ie=UTF-8'
# headers = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# response = requests.get(url=url, headers=headers)  # http запрос
#
# soup = BeautifulSoup(response.content, 'html.parser')
#
# weather = soup.findAll("span")
# print(f"weather: {weather}")


