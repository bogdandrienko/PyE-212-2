import threading
import time

import requests
from threading import Thread


# url = "https://www.gismeteo.kz/weather-pavlodar-5174/"
# headers = {
#     "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
# response = requests.get(
#     url=url,
#     headers=headers
# )
#
# data = response.content.decode()
# data1 = data.split('''"day">Сегодня''')[1]
# # data2 = data1.split('''Фактические данные''')[0]
# data2 = data1.split('''class="tab-image"''')[0]
#
# day_with_night = data2.split('''<span class="unit unit_temperature_c">''')
# # [1].split('''</span>''')[0]
# day_with_night = day_with_night[1::]  # c первого элемента(не с нулевого) : до конца : с шагом 1
#
# # print(day_with_night)
# # print(type(day_with_night))
# # print(len(day_with_night))
# #
# # for i in day_with_night:
# #     print(i, '\n')
#
# if len(day_with_night[0]) < len(day_with_night[1]):
#     day = day_with_night[1].split('''</span>''')[0]
#     night = day_with_night[0].split('''</span>''')[0]
# else:
#     day = day_with_night[0].split('''</span>''')[0]
#     night = day_with_night[1].split('''</span>''')[0]
#
# print(f'Днём температура: {day}, а ночью: {night}')
#
citys = [
    'https://www.gismeteo.kz/weather-shymkent-5324/',
    'https://www.gismeteo.kz/weather-pavlodar-5174/',
    'https://www.gismeteo.kz/weather-aktobe-5165/',
]


def decorator_vrema(func):
    def obertka(*args, **kwargs):
        time_func_start = time.perf_counter_ns()
        res = func(*args, **kwargs)
        print((time.perf_counter_ns() - time_func_start) // 1000000, 'ms')  # 1 000 000 000 ns 1 000 000 mk 1 000 ms 1 s
        return res

    return obertka


def request(url):
    headers = {
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(
        url=url,
        headers=headers
    )
    data = response.content.decode()
    data1 = data.split('''"day">Сегодня''')[1]
    data2 = data1.split('''class="tab-image"''')[0]
    day_with_night = data2.split('''<span class="unit unit_temperature_c">''')
    day_with_night = day_with_night[1::]
    if len(day_with_night[0]) < len(day_with_night[1]):
        day = day_with_night[1].split('''</span>''')[0]
        night = day_with_night[0].split('''</span>''')[0]
    else:
        day = day_with_night[0].split('''</span>''')[0]
        night = day_with_night[1].split('''</span>''')[0]
    print(f'{url}: Днём температура: {day}, а ночью: {night}')


@decorator_vrema
def sync_request():
    request(url=citys[0])
    request(url=citys[1])
    request(url=citys[2])


@decorator_vrema
def thread_request():
    thread_1 = Thread(target=request, args=(citys[0],))
    thread_2 = Thread(target=request, args=(citys[1],))
    thread_3 = Thread(target=request, args=(citys[2],))

    thread_1.start()
    thread_2.start()
    thread_3.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()


if __name__ == "__main__":
    # sync_request()  # 751 -> три по очереди
    thread_request()  # 264 -> три одновременно 250 * 3 = 750
