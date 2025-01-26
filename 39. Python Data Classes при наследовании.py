from typing import Any
from dataclasses import dataclass, field, InitVar, make_dataclass


@dataclass
class Goods:  # базовый класс
    current_uid = 0  # атрибут не аннотирован никаким типом, а значит декоратор @dataclass его пропустит, но он будет
    # существовать в классе Goods

    uid: int = field(init=False)  # uid будет формироваться автоматически при создании каждого нового объекта, его не
    # будет в инициализаторе
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print('Goods: post_init')
        Goods.current_uid += 1
        self.uid = Goods.current_uid


class GoodsMethodsFactory:
    @staticmethod  # Статические методы используются для выполнения задач, которые не зависят от состояния объекта или
    # класса. Чтобы вызвать статический метод, можно использовать как сам класс, так и его экземпляр
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Book(Goods):  # дочерний класс
    title: str = ''
    author: str = ''
    price: float = 0  # переопределенный атрибут
    weight: int | float = 0
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)  # добавление списка с габаритами,

    # который формируется в классе GoodsMethodsFactory, а благодаря default_factory будет уникальным для каждого
    # экземпляра класса

    def __post_init__(self):
        """Если есть __post_init__ в дочернем классе (Book), то он не будет вызван в базовом (Goods), т.к. идет его
        поиск снизу вверх. Поэтому мы можем вызвать __post_init__ базового класса явно через super"""
        super().__post_init__()
        print('Book: __post_init__')


"""При наследовании классов @dataclass в нашем случае их инициализаторы будут выглядеть так:
class Goods:
    def __init__(uid: Any, price: Any = None, weight: Any = None):
        pass

class Book:
    def __init__(self, uid: Any, price: float = 0, weight: int | float = 0, title: str = '', author: str = ''):
        pass
        
Не смотря на то, что price и weight аннотированы в классе Book 3 и 4 атрибутом, в __init__ они будут 2 и 3 атрибутом,
т.к. переопределены в базовом классе, а новые уникальные атрибуты (title и author) будут идти следом
"""

b1 = Book(1)
print(b1)  # Book(uid=1, price=1, weight=0, title='', author='', measure=[0, 0, 0])
b2 = Book(3, 4, 'Название книги', 'Автор книги')
print(b2)  # Book(uid=2, price=3, weight=4, title='Название книги', author='Автор книги', measure=[0, 0, 0])

"""make_dataclass

def make_dataclass(cls_name, fields, *, bases=(), namespace=None, init=True,
                   repr=True, eq=True, order=False, unsafe_hash=False,
                   frozen=False, match_args=True, slots=False):
                   
cls_name - название нового класса (в виде строки)
fields - поля (локальные атрибуты) объектов класса
* - произвольный набор позиционных аргументов
bases - список базовых классов
namespace - словарь для определения атрибутов самого класса (например, так можно объявлять методы класса)
"""


class Car:
    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed


"""При помощи make_dataclass создадим класс, подобный классу Car. Обычно это используется, когда есть потребность 
создания класса данных в процессе работы программы"""
CarData = make_dataclass('CarData', [('model', str), 'max_speed', ('price', float, field(default=0))],
                         namespace={'get_max_speed': lambda self: self.max_speed})

c = CarData('bmw', 256, 4096)
print(c)  # CarData(model='bmw', max_speed=256, price=4096)
print(c.get_max_speed())  # 256
