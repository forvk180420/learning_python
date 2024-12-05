"""
__str__() - для отображения информации об объекте класса для пользователей (print, str и т.д.)
__repr__() - для отображения информации об объекте класса в режиме отладки
__len__() - позволяет применять функцию len() к экземплярам класса
__abs__() - позволяет применять функцию abs() к экземплярам класса
"""


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        """Вывод информации об объекте класса в режиме отладки"""
        return f'{self.__class__}: {self.name}'  # __class__ - название класса

    # def __str__(self):
    #     """Вывод информации об объекте класса для пользователей"""
    #     return f'{self.name}'


cat = Cat("Васька")
print(cat)  # <class '__main__.Cat'>: Васька
"Если же раскоментить def __str__(self) в классе Cat, то:"
print(cat)  # Васька


class Point:
    """Если в классе явно не указать __len__ и __abs__, то len(p) и abs(p) (p - экземпляр класса) приведет к ошибке"""

    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, 2, -5)
print(len(p))  # 3
print(abs(p))  # [1, 2, 5]
