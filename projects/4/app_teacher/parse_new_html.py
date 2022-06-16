import bs4
import requests
from bs4 import BeautifulSoup

url = 'https://eda.ru/recepty/supy/borsch-mjasnoj-14622'
headers = {'User-agent': 'Mozilla/5.0'}
response = requests.get(url=url, headers=headers)
print(response.status_code)
# print(response.content.decode())
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())
print(type(soup))

data1 = soup.find_all('span', itemprop="text")
# data1 = soup.find_all('span', class_="text")
instructions = []
for i in data1:
    instructions.append(i.text)
    # print(i.text)
    # print(type(i.text))
# print(data1)
# print(type(data1))
print(instructions)

# print("\n \t \\ \"Рита\"")
