import openpyxl


class Tree:
    def __init__(self, age: float, name="Дуб"):  # инициализатор
        self.age = age
        self.name = name

        self.value1 = 10  # открытое свойство
        self._value2 = 10  # protected свойство
        self.__value3 = 10  # private свойство

    # def __new__(cls, *args, **kwargs):  # конструктор
    #     pass

    def __str__(self):  # строковое представление объекта
        return self.name

    def increase(self):
        value = self.__value3
        self.age += 1
        return self.age

    @staticmethod
    def increase_static(age: float):
        return age + 1.0


tree1 = Tree(15.4, "Сосна")


# print(tree1)
# print(type(tree1))
# print(tree1.age)
# print(tree1.increase())
# print(tree1.age)
# print(tree1._value2)
#
# print(Tree.increase_static(18.9))


class Dub(Tree):
    def __init__(self, age: float, name: str):
        super().__init__(age, name)

    def get_name(self):
        return self.name


tree2 = Dub(15.4, "Сосна")


# print(tree2.age)
# print(tree2.increase())
# print(tree2.age)
# print(tree2._value2)

#
#
#
#
#                 Транспортные средства
#            Сухопутные               Морские
#    машины       мотоциклы    подводные    наводные
# электро


class Transport:
    def __init__(self, name, mass, motor, price, speed):
        self.name = name
        self._mass = mass
        self.motor = motor
        self.price = price
        self.speed = speed  # публичная - видна во всех случаях

        self._multiplayer = 12  # защищённая - предупреждает, при попытке её извлечь вне собственного контекста
        self.__multiplayer = 10  # приватная - невидима везде, кроме собственного контекста

    def drive(self):
        return self._mass / self.motor

    def get_speed(self):
        return self.speed


Transport1 = Transport("Трактор", 2000, 400, 5000, 30)

print(Transport1)
print(type(Transport1))
print(Transport1.drive())
print(Transport1.speed)
print(Transport1._mass)
print(Transport1._multiplayer)


class Water(Transport):
    def __init__(self, speed, *args):
        super().__init__(*args)

        self.speed1 = speed

    def drive(self):
        return super().drive() / 0.85

    def get_old_speed(self):
        return super().get_speed()


Transport2 = Water(1000, "Катамаран", 500, 20, 700, 15)

print(Transport2)
print(type(Transport2))
print(Transport2.drive())
print(Transport2.speed)
print(Transport2.speed1)


class SubWater(Water):
    def __init__(self, *args, **kwargs):  # args - позиционные - кортеж, kwargs - именные - словарь
        super().__init__(*args, **kwargs)

    def drive(self):
        return super().drive() * 1.5


Transport3 = Water(333333, "Подлодка", 333, 33, 3333, 3)

dict1 = {"speed": 12}
val1 = dict1.get("speed", "")
val2 = dict1["speed"]

print(Transport3)
print(type(Transport3))
print(Transport3.drive())
print(Transport3.speed)
print(Transport3._mass)
print(Transport3.speed1)
print(Transport3.get_speed())

for key, _ in {"speed": 12, "title": "Car"}.items():  # -> ((key, value), (key, value))
    print(f"{key}")

wb = openpyxl.Workbook()
