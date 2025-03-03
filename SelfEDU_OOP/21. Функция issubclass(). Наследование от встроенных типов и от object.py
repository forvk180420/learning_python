"""
Пользовательский класс (например, Geom) по умолчанию наследуется от базового класса object.
Это сделано, чтобы обеспечить стандартный базовый функционал работы с классами.
"""


class Geom(object):
    """Наследование от самого базового класса object происходит автоматически с версии Python3, поэтому object можно
    не писать явно"""
    pass


class Line(Geom):
    """Цепочка наследования Line->Geom->object"""
    pass


print(Geom.__name__)  # Geom
g = Geom()
l = Line()

"""С помощью функции issubclass можно определить, является ли класс подклассом другого класса"""
print(issubclass(Line, Geom))  # True (1 аргумент - дочерний класс, 2 - базовый)
print(issubclass(Geom, Line))  # False

"""Если нужно проверить, принадлежность объекта тому или иному классу, то используется функция isinstance.
Отличие функции isinstance от issubclass в том, что issubclass работает только с классами, а isinstance может работать
и с объектами этих классов"""
print(isinstance(l, Geom))  # True
print(isinstance(l, object))  # True
print(isinstance(Geom, object))  # True
"""Все стандартные типы данных в Python (int, float, list, tuple, set и пр.) являются классами.
Это значит, что их функционал можно расширить, хотя применяется это крайне редко."""


class Vector(list):
    def __str__(self):
        return ' '.join(map(str, self))  # возврат строки, состоящей из элементов списка через пробел


v = Vector([1, 2, 3])
print(type(v))  # <class '__main__.Vector'>
