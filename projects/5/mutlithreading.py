import asyncio
import multiprocessing
import threading
import time
import datetime
import concurrent.futures
import requests
import aiohttp
import aiofiles


def decorator_time_measuring(function):  # ссылка на функцию

    def decorator(*args, **kwargs):
        time_start = datetime.datetime.now()
        print('before')

        result = function(*args, **kwargs)  # вызов функции из ссылки

        print('after')
        time_stop = datetime.datetime.now()

        print(time_stop - time_start)
        return result

    return decorator


def read_ints(path):
    lst = []
    with open(path, 'r') as file:
        while line := file.readline():
            lst.append(int(line))
    return lst


def count_sum(ints, thread_name):
    print(f"start thread: {thread_name}")

    n = len(ints) // 2
    counter = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Found in {thread_name}! Total: {counter}\n')
    print(f"end thread: {thread_name}, counter: {counter}")


@decorator_time_measuring
def run_parallel(ints):
    t1 = threading.Thread(target=count_sum, daemon=True, args=(ints, 't1'))
    t2 = threading.Thread(target=count_sum, daemon=True, args=(ints, 't2'))

    t1.start()
    t2.start()

    print('ожидание потоков')

    t1.join()  # дождаться завершения потока, т.е. не завершать главную функцию
    t2.join()  # дождаться завершения потока, т.е. не завершать главную функцию


@decorator_time_measuring
def run_sync(ints):
    count_sum(ints, 'main')
    count_sum(ints, 'main')


@decorator_time_measuring
def div(divisor, limit):
    print(f'start: {divisor}\n', end='\n')

    count = 0
    for x in range(1, limit):
        if x % divisor == 0:
            print(f'divisor {divisor}, x = {x}\n', end='\n')
            count += 1
        time.sleep(0.2)
    print(f'end {divisor}\n', end='\n')
    return count


@decorator_time_measuring
def threads():
    # div(3, 25)
    # div(3, 25)
    # div(3, 25)

    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #     executor.submit(div, 3, 25)
    #     executor.submit(div, 3, 25)
    #     executor.submit(div, 3, 25)
    #
    #     print('in with\n')

    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        futures = []
        for i in range(1, 4):
            future = executor.submit(div, 3, 25)
            futures.append(future.result())

        print('in with\n')
    #
    # print('out with\n')


# if __name__ == '__main__':
# print('start main')
#
# ints = read_ints('random_numbers.txt')
#
# run_parallel(ints)
# run_sync(ints)
#
# print('end main')

# threads()

# Грузить тяжёлую картинку / html - весь сайт с интернета и записывать в файл
# sync VS async VS threading VS multiprocessing

# sync = процесс 1: поток 1: грузим картинку 1, пишем картинку 1 в файл, грузим картинку 2...

# async = процесс 1: поток 1: грузим картинку 1, пока грузим картинку 1, начинаем грузить картинку 2, когда первая из
# картинок загрузилась пишем эту картинку в файл, затем остальные...

# threading = процесс 1: поток 1: грузим картинку 1, пишем картинку 1 в файл
# процесс 1: поток 2: грузим картинку 2, пишем картинку 2 в файл

# multiprocessing = процесс 1: грузим картинку 1, пишем картинку 1 в файл
# процесс 2: грузим картинку 2, пишем картинку 2 в файл

def measuring_time(function):
    def decorator(*args, **kwargs):
        time_start = time.perf_counter()
        result = function(*args, **kwargs)
        print(function, time.perf_counter() - time_start)
        return result

    return decorator


def task(task_name: str):
    print(f'BEGIN {task_name}', flush=True, end='\n')

    url = "https://picsum.photos/370/250"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    with open(f'temp/{task_name}_image.jpg', 'wb') as file:
        file.write(response.content)

    print(f'END {task_name}', flush=True, end='\n')
    return response


async def task_async(task_name: str):
    print(f'BEGIN {task_name}', flush=True, end='\n')

    async with aiohttp.ClientSession() as session:
        async with session.get("https://picsum.photos/370/250") as response:
            data = await response.read()
    with open(f'temp/{task_name}_image.jpg', 'wb') as file:
        file.write(data)

    print(f'END {task_name}', flush=True, end='\n')
    return response


@measuring_time
def sync_tasks():
    # start sync
    # task('sync_1')

    sync_list = [f'sync_{x}' for x in range(1, 11)]
    for sync in sync_list:
        task(sync)


def async_tasks():
    time_start = time.perf_counter()

    # start async
    # async def async_tasks_start():
    #     await asyncio.gather(task_async(f'async_1'))
    # asyncio.get_event_loop().run_until_complete(async_tasks_start())

    async def async_tasks_start():
        await asyncio.gather(
            *[task_async(f'async_{x}') for x in range(1, 11)]
        )

    asyncio.get_event_loop().run_until_complete(async_tasks_start())

    print('async', time.perf_counter() - time_start)


@measuring_time
def threading_tasks():
    # # define thread
    # thread_1 = threading.Thread(target=task, args=('thread_1',), kwargs={})
    # thread_2 = threading.Thread(target=task, args=('thread_2',), kwargs={})
    # # start thread
    # thread_1.start()  # start the task in a new thread
    # thread_2.start()  # start the task in a new thread
    # # join thread
    # thread_1.join()  # wait for the task to complete
    # thread_2.join()  # wait for the task to complete

    threading_list = [threading.Thread(target=task, args=(f'thread_{x}',), kwargs={}) for x in range(1, 11)]
    for thread in threading_list:
        thread.start()
    for thread in threading_list:
        thread.join()


@measuring_time
def process_tasks():
    # # define processes
    # process_1 = multiprocessing.Process(target=task, args=('process_1',), kwargs={})
    # process_2 = multiprocessing.Process(target=task, args=('process_2',), kwargs={})
    # # start processes
    # process_1.start()  # start the task in a new process
    # process_2.start()  # start the task in a new process
    # # join processes
    # process_1.join()  # wait for the task to complete
    # process_2.join()  # wait for the task to complete
    # # kill processes
    # process_1.terminate()  # wait for the task to complete
    # process_2.terminate()  # wait for the task to complete

    process_list = [multiprocessing.Process(target=task, args=(f'process_{x}',), kwargs={}) for x in range(1, 11)]
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()


# entry point for the program
if __name__ == '__main__':
    # async_tasks()  # 1.3329052
    # sync_tasks()  # 5.8510097
    # threading_tasks()  # 1.1851449
    # process_tasks()  # 1.1118587
    pass
