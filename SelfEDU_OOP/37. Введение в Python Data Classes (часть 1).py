"""Начиная с Python 3.7 появилась возможность создавать классы для хранения данных - Data Classes"""
from dataclasses import dataclass, field


class Thing:
    def __init__(self, name, weight, price=0):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        """Без этого print(t) будет <__main__.Thing object at 0x000002021EC74EB0>"""
        return f'Thing: {self.__dict__}'


t = Thing('Учебник', 100, 1024)

"""Сделаем практически идентичный классу Thing класс ThingData при помощи декоратора @dataclass"""


@dataclass
class ThingData:
    """Чтобы @dataclass срабатывал, обязательна аннотаиия типов.
    Здесь автоматически добавляется __repr__ и __init__
    Значения записываются по порядку
    Свойства с значением по умолчанию пишутся последними, аналогично как и для __init__(self, name, weight, price=0):

    Не следует в __init__ добавлять пустой список, т.к. __init__ будет одинаков для всех экземпляров класса, и, если
    в 1-м экз класса будет расширен этот список, то это всё пойдет и на другие экземпляры этого класса, аналогично и в
    @dataclass, но в dataclass нельзя по умолчанию и это вызовет исключение. Это касается не только списка, а любого
    изменяемого объекта.
    Чтобы всё же добавить список (или любой изменяемый объект) и сделать его различным для каждого экземпляра класса
    необходимо использовать функцию field"""
    name: str
    weight: int
    price: float = 0
    dims: list = field(default_factory=list)  # теперь для каждого экземпляра класса будут разные списки


td = ThingData('Учебник', 100, 1024)

print(t)  # Thing: {'name': 'Учебник', 'weight': 100, 'price': 1024}
print(td)  # ThingData(name='Учебник', weight=100, price=1024)
