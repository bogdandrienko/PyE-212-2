import openpyxl
from openpyxl import Workbook


# класс, который позволит считать периметр и площадь


class MyClass:
    def __init__(self, a, b, name='квадрат'):
        self.name = name
        self.a = int(a)
        if isinstance(b, str):
            b = int(b)
        self.b = b

    def get_perimeter(self):  # метод внутри класса, который работает с внутренними параметрами
        return self.a + self.b

    @staticmethod
    def get_perimeter_static(a, b):  # метод внутри класса, который работает с внутренними параметрами
        return a + b

    def get_square(self):  # метод внутри класса, который работает с внутренними параметрами
        return self.a * self.b

    @staticmethod
    def get_square_static(a, b):  # метод внутри класса, который работает с внутренними параметрами
        return a * b


# oop Калькулятор

class MyCalculator:
    def __init__(self, val1: float, val2: float):
        self.val1 = val1
        self.val2 = val2

    def sum1(self):
        return self.val1 + self.val2

    @staticmethod
    def sum1_static(val1: float, val2: float):
        print(val1 + val2)


if __name__ == "__main__":
    workbook = Workbook()
    worksheet = workbook.active
    worksheet["A1"] = '12'
    workbook.save('new.xlsx')

    print(workbook)
    print(type(workbook))

    print(MyClass)
    myclass = MyClass(name="Прямоугольник", b=15, a=15)  # создание экземпляра класса
    print(myclass)
    print(type(myclass))
    print(myclass.a)
    print(myclass.b)
    print(myclass.name)
    print(myclass.get_perimeter())
    print(myclass.get_square())
    print(MyClass.get_perimeter_static(17, 18))

    MyCalculator.sum1_static(20, 30.0)
    value = MyCalculator(30, 21.0).sum1()
    print(value)
else:
    pass
