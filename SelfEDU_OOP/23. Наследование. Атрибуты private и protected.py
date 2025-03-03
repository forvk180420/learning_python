"""
Режимы доступа:
attribute - публичное свойство (public)
_attribute - режим доступа protected (служит для обращения внутри класса и во всех его дочерних классах)
__attribute - режим доступа private (служит для обращения только внутри класса)
"""


class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'__init__ Geom для класса: {self.__class__}')
        self._x1 = x1
        self._y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_private_coords(self):
        """Внутри базового класса можно обращаться к защищенным атрибутам"""
        return (self.__x2, self.__y2)


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill

    """Внутри дочернего класса можно обращаться к защищенными атрибутами класса protected, но нельзя с приватными"""

    def get_protected_coords(self):
        return (self._x1, self._y1)


r = Rect(1, 2, 3, 4)

print(r.__dict__)  # {'_x1': 1, '_y1': 2, '_Geom__x2': 3, '_Geom__y2': 4, '_fill': 'red'} - к __x2 и __y2 добавляется
# _Geom
"""То есть, если вызвать r.__x2 - будет ошибка, но если вызвать r._Geom__x2, то ошибки не будет.
Однако, так делать не следует, потому что в случае изменения атрибута внутри класса при его обновлении, могут 
возникнуть ошибки"""
print(r._Geom__x2)  # 3
"Приватный же можно вызвать"
print(r._x1)  # 1

print(r.get_protected_coords())  # (1, 2)
print(r.get_private_coords())  # (3, 4)
