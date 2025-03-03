from dataclasses import dataclass, field, InitVar


class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = x + y + z if calc_len else 0


"""Провести работу с атрибутами класса, такую как self.length из класса Vector3D в @dataclass можно с помощью 
магического метода __post_init__"""


@dataclass
class V3D:
    x: int
    y: int
    z: int
    length: float = field(init=False)  # Атрибут length не будет добавлен как параметр в __init__

    def __post_init__(self):
        self.length = self.x + self.y + self.z


v = V3D(1, 2, 3)
"""Без length: float = field(init=False) в @dataclass при print(v) не будет length=6, но length=6 будет в __dict__"""
print(v)  # V3D(x=1, y=2, z=3, length=6)

"""Подробнее про функцию field:
repr - булевое значение указывает использовать ли атрибут в магическом методе __repr__()
compare - булевое значение указывает использовать ли атрибут при сравнении объектов
default - значение по умолчанию
"""


@dataclass
class V3D2:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    """Сделаем флаг calc_len, нужно ли выполнять вычисления length"""
    calc_len: InitVar[bool] = True  # параметры с InitVar автоматически передаются в метод __post_init__
    length: float = field(init=False, compare=False,
                          default=0)  # Атрибут length не будет добавлен как параметр в __init__ (init=False),

    # не будет учитываться при сравнении (compare=False), значение по умолчанию будет 0 (в нашем случае, если
    # флаг calc_len будет False)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = self.x + self.y + self.z


v1 = V3D2(1, 2, 3)
print(v1)  # V3D2(y=2, z=3, length=6) - здесь нет x, т.к. он был исключен из __repr__
v2 = V3D2(1, 2, 5)
"""Сравнив экземпляры класса v и v2"""
print(v1 == v2)  # True, т.к. мы исключили z и length из сравнения параметром compare
"""Сделаем флаг calc_len False, тогда вычисления length не будет и будет возвращено значение по умолчанию (0)"""
v3 = V3D2(1, 2, 3, False)
print(v3)  # V3D2(y=2, z=3, length=0)

"""Подробнее про параметры @dataclass, по умолчанию такие параметры:
def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
              unsafe_hash=False, frozen=False, match_args=True,
              kw_only=False, slots=False):
"""


@dataclass(init=False, repr=False, eq=False, order=False, frozen=True)
class V3D3:
    """Объяснение параметров в @dataclass :
    init=False - не будет формироваться инициализатор, пример: создание базового класса (обычно там нет init)
    repr=False - не будет магического метода repr
    eq=False - нельзя будет сравнивать экземпляры классов (будет False). Также нельзя будет прописывать собственные
    магические методы сравнения
    order=False - возможность сравнения на больше и меньше (>, >=, <, <=). Если order=True, то и eq=True, иначе ошибка
    frozen=True - замораживает значения локальных атрибутов, их нельзя будет менять после инициализации"""
    x: int
    y: int
    z: int
