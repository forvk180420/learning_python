class Point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = x + y

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


pt = Point2D(1, 2)
"""Не смотря на то, что локальное свойство должно называться __length, через @property можно обращаться по названию 
метода, т.к. по сути это атрибут класса, а не локальное свойство"""
print(pt.length)  # 3

"""Дочерний класс не наследует коллекцию __slots__, а значит, можно создавать локальные свойства в рамках экземпляра
наследуемого класса"""


class Point3:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point4(Point3):
    pass


pt4 = Point4(3, 4)
pt4.z = 5
print(pt4.__dict__)  # {'z': 5}
