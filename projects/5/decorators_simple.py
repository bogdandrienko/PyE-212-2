def decorator_rounding(func):  # определение декоратора -> ссылку на функцию
    def decorator(*args, **kwargs):  # передача аргументов к вызову функции
        # print(args)
        # print(kwargs)

        # BEFORE - корректировка результата перед отработкой функции
        positive_list = []
        for arg in args:
            if arg < 0:
                arg = arg * -1
            positive_list.append(arg)
        # positive_list = [x for x in args if (x < 0)]
        # print(positive_list)
        args = tuple(positive_list)
        # print(args)
        # BEFORE - корректировка результата перед отработкой функции

        result = func(*args, **kwargs)  # вызов функции

        # AFTER - корректировка результата после отработки функции
        result = round(result, 2)
        # AFTER - корректировка результата после отработки функции

        return result  # возврат результата функции
    return decorator  # возврат декоратора


@decorator_rounding  # добавление декоратора
def summing(value1, value2, value3):  # определение функции
    res = value1 + value2 + value3  # расчёт функции
    return res  # возврат результата функции


@decorator_rounding  # добавление декоратора
def divider(value1, value2):  # определение функции
    res = value1 / value2  # расчёт функции
    return res  # возврат результата функции


total = summing(-12, 17.0006, 1)  # вызов функции
print(total)  # вывод результата

total = divider(12, -17)  # вызов функции
print(total)  # вывод результата
