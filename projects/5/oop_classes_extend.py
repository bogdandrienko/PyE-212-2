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
print(tree1)
print(type(tree1))
print(tree1.age)
print(tree1.increase())
print(tree1.age)
print(tree1._value2)

print(Tree.increase_static(18.9))


class Dub(Tree):
    def __init__(self, age: float, name: str):
        super().__init__(age, name)

    def get_name(self):
        return self.name


tree2 = Dub(15.4, "Сосна")
print(tree2.age)
print(tree2.increase())
print(tree2.age)
print(tree2._value2)
