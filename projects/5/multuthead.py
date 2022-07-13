# Грузить тяжёлую картинку / html - весь сайт с интернета и записывать в файл
# sync VS async VS threading VS multiprocessing

# sync = процесс 1: поток 1: грузим картинку 1, пишем картинку 1 в файл, грузим картинку 2...

# async = процесс 1: поток 1: грузим картинку 1, пока грузим картинку 1, начинаем грузить картинку 2, когда первая из
# картинок загрузилась пишем эту картинку в файл, затем остальные...

# threading = процесс 1: поток 1: грузим картинку 1, пишем картинку 1 в файл
# процесс 1: поток 2: грузим картинку 2, пишем картинку 2 в файл

# multiprocessing = процесс 1: грузим картинку 1, пишем картинку 1 в файл
# процесс 2: грузим картинку 2, пишем картинку 2 в файл
import time

import requests

import threading

import multiprocessing

import asyncio
import aiohttp


def measure_sync(func):
    def decorator(*args, **kwargs):
        time_start = time.perf_counter()
        result = func(*args, **kwargs)
        print(time.perf_counter() - time_start)
        return result

    return decorator


@measure_sync
def tick(secs: float):
    print('hello!')
    time.sleep(secs)
    print('bye!')

    return "123"


def task(task_name: str):
    print(f'BEGIN {task_name}\n', end='\n')

    response = requests.get(
        url="https://picsum.photos/370/250",
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
    )
    with open(f'temp/{task_name}_image.jpg', 'wb') as file:
        file.write(response.content)

    print(f'END {task_name}\n', end='\n')


@measure_sync
def sync_task():
    # task(f"sync_1")

    for i in range(1, 11):
        task(f"sync_{i}")


@measure_sync
def threading_task():
    # thread = threading.Thread(target=task, args=(f"thread_1",), kwargs={})
    # thread.start()
    # thread.join()

    thread_list = [threading.Thread(target=task, args=(f"thread_{x}",), kwargs={}) for x in range(1, 101)]
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()


@measure_sync
def processing_task():
    # process = multiprocessing.Process(target=task, args=(f"process_1",), kwargs={})
    # process.start()
    # process.join()

    processing_list = [multiprocessing.Process(target=task, args=(f"process_{x}",), kwargs={}) for x in range(1, 101)]
    for processing in processing_list:
        processing.start()
    for processing in processing_list:
        processing.join()


async def async_t(task_name: str):
    print(f'BEGIN {task_name}\n', end='\n')

    async with aiohttp.ClientSession() as session:
        async with session.get(
                url="https://picsum.photos/370/250",
                headers={
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/102.0.0.0 Safari/537.36'
                }
        ) as response:
            data = await response.read()

    with open(f'temp/{task_name}_image.jpg', 'wb') as file:
        file.write(data)

    print(f'END {task_name}\n', end='\n')

    return response


def async_task():
    time_start = time.perf_counter()

    async def async_task_asyncio():  # корутина
        await asyncio.gather(
            *[async_t(f"async_{x}") for x in range(1, 101)]
        )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_task_asyncio())

    print(time.perf_counter() - time_start)


def test(thread: str):
    print(f'Thread(process) {thread} started\n')

    time.sleep(3)

    print(f'Thread(process) {thread} ended\n')


@measure_sync
def start_test():
    # sync
    # for x in range(1, 4):
    #     test(str(x))

    # thread
    # thread_1 = threading.Thread(target=test, args=(f"1",), kwargs={})
    # thread_2 = threading.Thread(target=test, args=(f"2",), kwargs={})
    # thread_3 = threading.Thread(target=test, args=(f"3",), kwargs={})
    #
    # thread_1.start()
    # thread_2.start()
    # thread_3.start()
    #
    # thread_1.join()
    # thread_2.join()
    # thread_3.join()

    # process
    # process_1 = multiprocessing.Process(target=test, args=(f"1",), kwargs={})
    # process_2 = multiprocessing.Process(target=test, args=(f"2",), kwargs={})
    # process_3 = multiprocessing.Process(target=test, args=(f"3",), kwargs={})
    #
    # process_1.start()
    # process_2.start()
    # process_3.start()
    #
    # process_1.join()
    # process_2.join()
    # process_3.join()

    pass


if __name__ == '__main__':
    # sync_task()  # 60.3940136 # 1 поток, 1 процесс
    # threading_task()  # 3.0885683  # N поток, 1 процесс
    # processing_task()  # 14.199895  # N поток, N процесс
    # async_task()  # 5.6319412  # 1 поток, 1 процесс

    start_test()
    pass
