"""
Метакласс - это самый верхний по иерархии класс (объект), от которого наследуются все другие классы (объекты).
Также метакласс это type(object), от которого происходит всё в языке Python
"""


class Point:
    MAX_COORD = 100
    MIN_COORD = 0


"""Создадим динамически при помощи type класс, аналогичный классу Point
где Point2 - имя класса, () - кортеж из базовых классов для наследования, 
{'MAX_COORD': 100, 'MIN_COORD': 0} - атрибуты класса
"""
P = type('Point2', (), {'MAX_COORD': 100, 'MIN_COORD': 0})

print(P)  # <class '__main__.Point2'>

p2 = P()
print(p2.MAX_COORD)  # 100

"""Пример динамического создания класса с наследованием, атрибутами и методами"""


class B1: pass


class B2: pass


def method1(self):
    print(self.__dict__)


P3 = type('Point3', (B1, B2), {'MAX_COORD': 100, 'MIN_COORD': 0, 'method1': method1})

p3 = P3()
p3.method1()  # {} - сработало корректно
