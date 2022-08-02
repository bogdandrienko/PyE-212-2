def checkpolidrom(value1: str) -> bool:
    # val1, val2 = value1, value1[::-1]
    if value1 == value1[::-1]:
        return True
    else:
        return False


print(checkpolidrom("голод 1долог"))
print("run"[::])  # - пересобирает строку кроме последнего символа
print("run"[-1])  # - берёт последний символ


def recur_sum(max_val: int) -> None:
    if max_val < -100:
        return None
    else:
        print(max_val)
        recur_sum(max_val - 1)  # 9 8 7 6


# recur_sum(10)


def getfactorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):  # [1, 2, 3, 4, 5]
        res *= i
    return res


print(getfactorial(3))  # 3 628 800


def getfactorial1(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * getfactorial1(n - 1)  # (4, 5)


print(getfactorial1(4))  # 3 628 800
