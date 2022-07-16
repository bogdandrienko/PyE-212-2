import time
import threading
import multiprocessing
import asyncio

import requests

from multuthead import measure_sync


def test(thread: str):
    print(f'Thread(process) {thread} started\n')
    time.sleep(3)
    print(f'Thread(process) {thread} ended\n')


async def async_test(thread: str):
    print(f'Thread(process) {thread} started\n')
    await asyncio.sleep(3)
    print(f'Thread(process) {thread} ended\n')


@measure_sync
def start_test():
    # sync
    # test(str('1'))
    # test(str('2'))
    # test(str('3'))

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

    # asyncio.get_event_loop().run_until_complete(
    #     asyncio.gather(
    #         *[async_test(str('1')), async_test(str('2')), async_test(str('3'))]
    #     )
    # )

    pass


def mes(func):
    def wrap(*args, **kwargs):
        # kwargs["value"] = kwargs["value"] // 2

        # args (10, 5, 6)
        # args[0] 10
        # args[0]//2 5
        # args[1:] (5, 6)
        # (args[0]//2, args[1:],) (5, 5, 6)
        args = (args[0]//2, args[1:],)
        #
        # перехват данных до
        #

        result = func(*args, **kwargs)

        #
        # обработка данных после
        #

        # page = 2
        # limit = 3
        #
        # [["1", "2", "3"], ["4", "5", "6"], ["7", "7"]]
        # ["4", "5", "6"]

        # for i in result:
        #     print(f"record= " + str(result.index(i)+1))
        #     print(f"page= " + str(result.index(i) // 10 + 1))

        return result

    return wrap


@mes
def get_data(value=6, val2=1, val3=1):
    print(value)
    url = 'https://jsonplaceholder.typicode.com/todos/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(
        url=url,
        headers=headers
    )
    print(response.json(), '\n')
    return response.json()


if __name__ == '__main__':
    time1 = time.perf_counter()
    # start_test()
    # res1 = get_data(value=4)

    thread1 = threading.Thread(target=get_data, args=(10, 5, 6))
    thread1.start()

    thread2 = threading.Thread(target=get_data, args=(10, 5, 6))
    thread2.start()

    thread3 = threading.Thread(target=get_data, args=(10, 5, 6))
    thread3.start()

    thread4 = threading.Thread(target=get_data, args=(10, 5, 6))
    thread4.start()

    thread5 = threading.Thread(target=get_data, args=(10, 5, 6))
    thread5.start()

    thread6 = threading.Thread(target=get_data, args=(10, 5, 6))
    thread6.start()

    res1 = get_data(10, 5, 6)
    res2 = get_data(10, 5, 6)
    res3 = get_data(10, 5, 6)
    res4 = get_data(10, 5, 6)
    res5 = get_data(10, 5, 6)
    res6 = get_data(10, 5, 6)

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()

    print(time.perf_counter()-time1)