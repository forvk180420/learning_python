class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MAX_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def set_bound_self(self, left):
        self.MIN_COORD = left  # изменение атрибута будет в рамках экземпляра класса

    @classmethod
    def set_bound_(cls, right):
        cls.MIN_COORD = right  # изменение атрибута класса

    def __getattribute__(self, item):
        """Этот метод автоматически вызывается, когда идет получение атрибута через экземпляр класса.
        Мы же явно переопрделяем его.
        Это нужно, например, чтобы запретить доступ к определенному атрибуту"""
        print('__getattribute__')
        if item == "y":
            raise ValueError('Доступ запрещен')
        else:
            return object.__getattribute__(self, item)  # переопределили магический метод

    def __setattr__(self, key, value):
        """Автоматически вызывается в момент присвоения какому-либо атрибуту определенного значения.
        Это нужно, например, чтобы запретить создавать какой-либо локальный атрибут в экземплярах класса"""
        print('__setattr__')
        if key == 'z':
            raise AttributeError('Недопустимое имя атрибута')
        else:
            object.__setattr__(self, key, value)
            """Особенноть: нужно недопустить возникновения рекурсии"""
            # self.x = value
            "Можно так:"
            self.__dict__[key] = value  # но, лучше и этого избегать

    def __getattr__(self, item):
        """Автоматически вызывается каждый раз, когда идет обращение к несуществующему атрибуту экземпляра класса
        Это нужно, например, чтобы при обращении к несуществующему атрибуту экземпляра класса возвращалось False,
        а не исключение"""
        return False

    def __delattr__(self, item):
        """Автоматически вызывается каждый раз, когда удаляется определенный атрибут из экземпляра класса
        Это нужно, например, чтобы контролировать процесс удаления атрибутов экземпляра класса"""
        object.__delattr__(self, item)


pt1 = Point(1, 2)
a = pt1.x  # __getattribute__
print(a)  # 1

"""__getattribute__ Попытка доступа к запрещенному атрибуту
b = pt1.y  # ValueError: Доступ запрещен
"""

"""__setattr__
pt1.z = 5  # AttributeError: Недопустимое имя атрибута
"""

"""__getattr__"""
print(pt1.yy)  # False
