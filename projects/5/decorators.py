import time
import datetime
from collections import OrderedDict


# @staticmethod

def decorator_time_measuring(function):  # ссылка на функцию
    def decorator(*args, **kwargs):
        time_start = datetime.datetime.now()
        print('before')

        if "author" in kwargs:
            kwargs["author"] = "Кролик"

        result = function(*args, **kwargs)  # вызов функции из ссылки

        print(f"PRINT RESULT IN DECORATOR: {result}")
        result = f'{result} 11111111'

        print('after')
        time_stop = datetime.datetime.now()
        time_difference = time_stop - time_start
        print(time_difference)

        return result

    return decorator


@decorator_time_measuring
def function_something_write(value: int):
    time.sleep(0.15)
    print("function_something_write")  # Ядро функции 1

    return value


@decorator_time_measuring
def function_something_read():
    time.sleep(0.07)
    print("function_something_read")  # Ядро функции 2

    return ['12', 124325]


@decorator_time_measuring
def function_something_analyse(author: str, title: str):
    time.sleep(0.12)
    print("function_something_analyse")  # Ядро функции 2

    return f'155: {author} | {title}'


print("\n ************ \n")
ret1 = function_something_write(6666)  # args
print('!!!!!!!!', ret1)
print("\n ************ \n")
ret2 = function_something_read()
print('!!!!!!!!', ret2)
print("\n ************ \n")
dict1 = {
    "title": "Борщ",
    "author": 'Alice',
}
# ret3 = function_something_analyse(title="Борщ", author='Alice')  # kwargs
ret3 = function_something_analyse(**dict1)  # kwargs
print('!!!!!!!!', ret3)
print("\n ************ \n")


# Логирование времени исполнения функции

# DRY - don't repeat yourself


def calculate_sum(value1, value2):
    return value1 + value2


def calculate_sum_many(*args):
    result = 0
    for arg in args:
        result += arg
    return result


print("\n ************ \n")

# lst = [1, 2]
# result = calculate_sum(lst[0], lst[1])
# result = calculate_sum(*lst)
# print(f'result: {result}')

lst = [x for x in range(1, 100 + 1)]  # [1, 2,3 ... 100]
# print(*lst)
result = calculate_sum_many(*lst)
print(f'result: {result}')

print("\n ************ \n")

a = [1, 2, 3]
b = [4, 5, 6]

c = [b, a]  # [[4, 5, 6], [1, 2, 3]]
c = [*b, *a]  # [4, 5, 6, 1, 2, 3]
print(c)

query_1 = [
    {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    },
    {
        "userId": 1,
        "id": 2,
        "title": "quis ut nam facilis et officia qui",
        "completed": False
    },
    {
        "userId": 1,
        "id": 3,
        "title": "fugiat veniam minus",
        "completed": False
    },
    {
        "userId": 1,
        "id": 4,
        "title": "et porro tempora",
        "completed": True
    }
]

query_2 = [
    {
        "userId": 2,
        "id": 23,
        "title": "et itaque necessitatibus maxime molestiae qui quas velit",
        "completed": False
    },
    {
        "userId": 2,
        "id": 24,
        "title": "adipisci non ad dicta qui amet quaerat doloribus ea",
        "completed": False
    },
    {
        "userId": 2,
        "id": 25,
        "title": "voluptas quo tenetur perspiciatis explicabo natus",
        "completed": False
    },
    {
        "userId": 2,
        "id": 26,
        "title": "aliquam aut quasi",
        "completed": False
    },
    {
        "userId": 2,
        "id": 27,
        "title": "veritatis pariatur delectus",
        "completed": False
    },
]

# main_query = []
# for i in query_1:
#     main_query.append(i)
# for i in query_2:
#     main_query.append(i)
main_query = [*query_2, *query_1]
# print(main_query)


print("\n ************ \n")


def print_sms(time, author, sms):
    print(f"author: {author}, sms: {sms}, time: {time}")


print_sms(author="Alice", time="10:44", sms="hiiii")

dict1 = {
    "author": "Alice",
    "sms": "Hi!",
    "time": "21:30"
}
# print_sms(author=dict1["author"], sms=dict1["sms"], time=dict1["time"])  # author: Alice, sms: hiiii, time: 10:44
print_sms(*dict1)  # author: sms, sms: time, time: author
print_sms(**dict1)  # author: Alice, sms: Hi!, time: 21:30

# for key, value in dict1.items():
#     print(f'{key} : {value}')

# def print_sms_dict(dict2):
#     author = dict2["author"]
#     time = dict2["time"]
#     sms = dict2["sms"]
#
#     print(f"1111 author: {author}, sms: {sms}, time: {time}")
# print_sms_dict(dict2=dict1)
# numbers = OrderedDict({"one": 1, "two": 2, "three": 3})
