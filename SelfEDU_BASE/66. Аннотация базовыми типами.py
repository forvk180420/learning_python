""""В Python динамическая типизация, но можно указать ее явно. Это не влияет ни на что, кроме визуала"""

cnt: int
cnt = 1
cnt = -4.4  # Подчеркивание: Expected type 'int', got 'float' instead (Ожидается int, а здесь float)

cnt2: int = 0  # более краткая запись


def mul2(x: int) -> int:  # чаще аннотация применяется в функциях. Теперь при вызове x. выйдет набор аттрибутов для int,
    #  -> int - это то, что возвращает функция
    return x * 2


res = mul2(5)
print(res)  # 10
res2 = mul2('s')  # Expected type 'int', got 'str' instead
print(res2)  # ss

print(mul2.__annotations__)  # {'x': <class 'int'>, 'return': <class 'int'>} (параметры функции, которые аннотированы)


def show_x(x: float) -> None:  # Если функция ничего не возвращает, то она возвращает None. Это указано явно.
    print(f'x={x}')


print(show_x.__annotations__)  # {'x': <class 'float'>, 'return': None}

"""Более сложная аннотация"""
from typing import Union, Optional, Any, Final

"""Union - объединение"""


def dd(x: Union[int, float]):  # объединение типов аннотации (вместо union можно так: int | float)
    print(x)


"""Можно Union использовать как переменную """
u = Union[int, float]  # и в функции использовать просто u. Лучше этим не увлекаться.

"""Optional - можно указать только 1 тип данных, а также к нему будет добавлен None автоматически"""

Str = Optional[str]
StrType = Union[str, None]  # Str и StrType это одно и тоже

"""Any - любой тип данных. Нужно, чтобы явно указать об этом."""

"""Final - константа"""
MAX_VAL: Final = 1000
MAX_VAL = 200  # 'MAX_VAL' is 'Final' and could not be reassigned
