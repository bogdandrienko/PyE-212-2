import requests
from bs4 import BeautifulSoup


url = "https://www.google.com/search?q=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&rlz=1C1IXYC_ruKZ978KZ978&oq=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&aqs=chrome.0.0i433i512j0i512l9.4659j1j7&sourceid=chrome&ie=UTF-8"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
}
response = requests.get(url=url, headers=headers)

print(response.content.decode())
print(type(response.content.decode()))

soup = BeautifulSoup(response.content, 'html.parser')
valute = soup.findAll("span", {"class": "UMOHqf EDgFbc"})[0]

print(f"valute: {valute.get_text()}")
print(f"valute type: {type(valute.get_text())}")

kurs = float(str(valute.get_text()).split('отметки')[1].split('тенге')[0].strip())
print(f"kurs: {kurs}")
print(f"kurs type: {type(kurs)}")

tenge = float(input("Введите сколько у Вас есть денег в тенге?"))

dollar = round(tenge / kurs, 2)

print(f'Ваши деньги в долларах: {dollar}')

