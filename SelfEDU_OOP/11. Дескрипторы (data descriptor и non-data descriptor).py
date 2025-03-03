"""
Дескрипторы — это объекты, которые позволяют управлять доступом к атрибутам других объектов. Они используются, чтобы
добавить дополнительную логику при чтении, записи или удалении атрибута.

Дескрипторы бывают двух типов:
Data Descriptor (дескриптор данных) — управляет чтением и записью атрибута.
Non-Data Descriptor (не-дескриптор данных) — управляет только чтением атрибута.

Дескриптор — это объект, который реализует один или несколько из этих методов:
__get__: Вызывается, когда вы пытаетесь получить значение атрибута.
__set__: Вызывается, когда вы пытаетесь установить значение атрибута.
__delete__: Вызывается, когда вы пытаетесь удалить атрибут.
"""


class UpperCaseDescriptor:
    """это дескриптор"""

    def __get__(self, instance, owner):
        return self.value.upper()

    def __set__(self, instance, value):
        self.value = value


class Person:
    name = UpperCaseDescriptor()  # это атрибут класса Person, который управляется дескриптором.


# Создаем объект
person = Person()
person.name = "alex"  # Вызовется __set__
print(person.name)  # Вызовется __get__ и вернет "ALEX"

"""Non-Data Descriptor Реализует только метод __get__, Не имеет приоритета над атрибутами экземпляра"""


class NonDataDescriptor:
    def __get__(self, instance, owner):
        return "Non-Data Descriptor"


class MyClass:
    attr = NonDataDescriptor()


obj = MyClass()
print(obj.attr)  # Вызовется __get__
obj.attr = 10  # Создаст новый атрибут в экземпляре
print(obj.attr)  # Выведет 10, а не вызовет __get__

"""
Когда Python ищет атрибут, он действует в таком порядке:
Data Descriptor: Если атрибут является дескриптором данных, вызывается его метод __get__.
Атрибуты экземпляра: Если атрибут не является дескриптором данных, Python ищет его в экземпляре.
Non-Data Descriptor: Если атрибут не найден в экземпляре, вызывается метод __get__ не-дескриптора.
Атрибуты класса: Если атрибут не найден в экземпляре и не является дескриптором, Python ищет его в классе.

Дескрипторы полезны, когда нужно:
Добавить проверку значений (например, чтобы возраст не был отрицательным).
Логировать доступ к атрибутам.
Создавать вычисляемые свойства (например, площадь прямоугольника на основе его сторон).
Управлять доступом к данным (например, в ORM, как в Django или SQLAlchemy).
"""

"""(SelfEDU) Дескрипторы в Python — это механизм, позволяющий управлять доступом к атрибутам объекта через специальные методы.
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
