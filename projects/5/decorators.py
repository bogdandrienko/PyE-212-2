import time
import datetime


# @staticmethod

def decorator_time_measuring(function):  # ссылка на функцию
    def decorator():
        time_start = datetime.datetime.now()
        print('before')

        function()  # вызов функции из ссылки

        print('after')
        time_stop = datetime.datetime.now()
        time_difference = time_stop - time_start
        print(time_difference)

    return decorator


@decorator_time_measuring
def function_something_write():
    time.sleep(0.15)
    print("function_something_write")  # Ядро функции 1


@decorator_time_measuring
def function_something_read():
    time.sleep(0.07)
    print("function_something_read")  # Ядро функции 2


@decorator_time_measuring
def function_something_analyse():
    time.sleep(0.12)
    print("function_something_analyse")  # Ядро функции 2


print("\n ************ \n")
function_something_write()
print("\n ************ \n")
function_something_read()
print("\n ************ \n")
function_something_analyse()
print("\n ************ \n")

# Логирование времени исполнения функции

# DRY - don't repeat yourself
