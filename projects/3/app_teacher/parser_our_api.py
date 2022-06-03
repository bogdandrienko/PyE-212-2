import requests
import json

url = 'http://127.0.0.1:8000/teacher/user_count/'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
response = requests.get(url=url, headers=headers)  # http запрос
html_data = json.loads(response.content)  # превращает байты в словарь (JSON)
print(html_data)
print(type(html_data))
