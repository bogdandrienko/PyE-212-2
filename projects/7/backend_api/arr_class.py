class Mother:
    val1 = 12

    def __init__(self, val1, name="Мама") -> None:
        self.name = name
        self.val = val1
        self._val = val1  # защищённый
        self.__val2 = val1 + 5  # приватный

    def get_value2(self):
        return 10

    def __str__(self):
        return self.name


class Father:
    val2 = 13

    def __init__(self, val1) -> None:
        self.val1 = val1

    def get_value(self):
        return 8

    def __str__(self):
        return self.val1


class Child(Mother, Father):

    def __init__(self, val1) -> None:
        super().__init__(val1)

    def get_value1(self):
        return 5


print(Mother.val1)
a1 = Mother(10)
print(a1.val)
# print(a1._Mother__val2)

ch1 = Child(10)
print(ch1.get_value())
