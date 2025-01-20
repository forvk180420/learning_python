"""Пользовательские метаклассы можно создавать для удобства использования

Зачем нужны метаклассы?
Метаклассы полезны, когда нужно модифицировать поведение или структуру классов на этапе их создания. Примеры:

Валидация классов: Проверка, что класс имеет определенные атрибуты или методы.
Автоматизация: Автоматическое добавление атрибутов или методов.
Логирование: Логирование информации при создании классов.
ORM (Object-Relational Mapping): Многие библиотеки используют метаклассы для динамического создания классов.
"""


def create_class_point(name, base, attrs):
    """Это простейший пользовательский метакласс,
    где name - имя, base - кортеж наследуемых классов, attrs - атрибуты класса"""
    attrs.update({'MAX_COORD': "100"})
    return type(name, base, attrs)


class Point(metaclass=create_class_point):
    """Создание класса Point по образу и подобию create_class_point,
    к нему принадлежат атрибут attrs с MAX_COORD и метод get_coords"""

    def get_coords(self):
        return (0, 0)


pt = Point()
print(pt.MAX_COORD)  # 100
print(pt.get_coords())  # (0, 0)

"""Чаще используют metaclass=ДругойКласс, чем функцию"""


class Meta(type):
    def __new__(cls, name, base, attrs):  # cls - это ссылка на уже созданный класс Pont2
        cls.MAX_COORD = 100  # динамическое добавление атрибута
        return super().__new__(cls, name, base, attrs)


class Pont2(metaclass=Meta):
    """В коллекцию attrs будут переданы все атрибуты (в данном случае метод get_coords)"""

    def get_coords(self):
        return (0, 0)

pt2 = Pont2()
pt2.get_coords()