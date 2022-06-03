import requests


def get():
    url = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&rlz=1C1IXYC_ruKZ978KZ978&oq=gjujlf&aqs=chrome.1.69i57j0i10i131i433l9.1695j1j7&sourceid=chrome&ie=UTF-8'
    response = requests.get(url)
    return response.content.decode()

# print(get())
