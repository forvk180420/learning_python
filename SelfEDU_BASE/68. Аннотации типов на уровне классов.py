from __future__ import  annotations
from typing import Any, Type, TypeVar

tr: dict = {'car': 'машина'}

x: object = None
x = '123'
x = 123

"""object  - это базовый класс для всех остальных классов"""


class Geom: pass


class Line(Geom): pass


g: Geom
g = Line()

"""
Почему бы вместо object не использовать ANY?
Тип ANY совместим с любым другим типом, а тип object - ни с кем другим
"""

a: Any = None
s: str
s = a

"""
Если в примере выше вместо Any использовать object, то будет ошибка с точки зрения аннотации, 
т.к. str наследуется от object
Т.е. к object привести str можно, а наоборот - нельзя.
"""


class Point2D(Geom):
    x: int
    y: int

    def __int__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def copy(self) -> Point2D:
        return Point2D(self.x, self.y)


p = Point2D(10, 20)
p.x = '10'

T = TypeVar('T', bound=Geom)  # bound - ограничения
T = TypeVar('T', int, float)


def factory_object(cls_obj: Type[T]) -> T:
    return cls_obj()


geom: Geom = factory_object(Geom)
point: Point2D = factory_object(Point2D)
