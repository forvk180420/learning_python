"""Дескрипторы в Python — это механизм, позволяющий управлять доступом к атрибутам объекта через специальные методы.
Это мощный инструмент для настройки поведения атрибутов, например, для их вычисления «на лету», проверки,
преобразования, кэширования или контроля доступа."""


class Integer:
    """Это класс дескриптор с данными, предназначен для альтернативы property. Применяется для сокращения кода в случае
    функционального повтора, когда применение property излишне"""

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом')

    def __set_name__(self, owner, name):
        """
        Магический метод set_name автоматически вызывается при создании экземпляра класса для создания локального
        атрибута ('_' + имя)
        self - ссылка на создаваемый экземпляр класса
        owner - ссылка на класс (Point3d)
        name - это имя экземпляра класса (x, y, z)
        """
        self.name = '_' + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name] # равносильные строки, но с точки зрения Python правильно getattr
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """
        self - ссылка на создаваемый экземпляр класса
        instance - ссылка на экземпляр класса (pt = Point3d), из которого этот дескриптор был вызван
        value - числовое значение, которое присваивается при создании экземпляра класса
        """
        print(f'__set__: {self.name} = {value}')
        self.verify_coord(value)  # проверка координаты
        # instance.__dict__[self.name] = value  # формируем локальное свойство (_x, _y, _z)
        setattr(instance, self.name, value)  # равносильная строка, но с точки зрения Python правильно setattr


class ReadIntX:
    """Дескрипторы не данных (non-data descriptor) """

    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Point3d:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3d(1, 2, 3)
# __set__: _x = 1
# __set__: _y = 2
# __set__: _z = 3
print(p.__dict__)
# {'_x': 1, '_y': 2, '_z': 3}
print(p.z)  # 3
print(p.xr)
