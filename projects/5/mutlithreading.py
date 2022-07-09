import threading
import time
import datetime
import concurrent.futures


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
from multiprocessing import Process


# a task to execute in another process
def task(process_name: str, time_to_sleep: float):
    print(f'This is start another process {process_name}', flush=True, end='\n')
    time.sleep(time_to_sleep)
    print(f'This is end another process {process_name}', flush=True, end='\n')


# entry point for the program
if __name__ == '__main__':
    p1 = Process(target=task, args=('p1', 3.5))  # define a task to run in a new process
    p1.start()  # start the task in a new process

    p2 = Process(target=task, args=('p2', 6.5))  # define a task to run in a new process
    p2.start()  # start the task in a new process

    p3 = Process(target=task, args=('p3', 5.5))  # define a task to run in a new process
    p3.start()  # start the task in a new process



    p1.join()  # wait for the task to complete
    p2.join()  # wait for the task to complete
    p3.join()  # wait for the task to complete
