"""
Магические методы или dunder-методы (от анг. double underscope)
Магический метод __call__ служит для вызова класса c = Counter() - речь про скобки, т.е. возможность вызова
"""
import math


class Counter:
    def __init__(self):
        self.__counter = 0


c = Counter()  # Скобки в общем случае это оператор вызова функции, а в данном случае класса
"""
Сначала вызывается __call__, затем __new__, __init__ 
"""
# с() - будет ошибка, потому как экземпляры класса вызывать через оператора вызова функции (__call__) не можем, т.к.
# в классе Counter магический метод __call__ не вызван явно

"Вызовем __call__ явно"


class Counter2:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print('__call__')
        self.__counter += 1
        return self.__counter


# теперь можно вызвать (речь о скобках) из оператора вызова функции (__call__)
c2 = Counter2()
c2()  # __call__ (ошибки нет, т.к. в классе Counter2 магический метод __call__ задан явно
"""Если экземпляры класса можно вызывать подобно функциям, то этот класс называется ФУНКТОРОМ"""
c2()
c2()
res = c2()
print(res)  # 4 (т.е. при каждом вызове срабатывает метод __call__, выводится print и каждый раз увеличивается счетчик
"Можно создать несколько независимых счетчиков"
c3 = Counter2()
res3 = c3()
print(res3)  # 1


class StripChars:
    """Функторы могут использоваться как альтернатива замыканиям"""

    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')
        return args[0].strip(self.__chars)


s1 = StripChars('&?:!.;')
print(s1('Hi!!?'))  # Hi
s2 = StripChars(' ')
print(s2(' hello    '))  # hello


class Derivate:
    """Функторы могут использоваться для создания декораторов на основе класса"""

    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate
def df_sin(x):
    return math.sin(x)


print(df_sin(math.pi / 3))  # 0.4999566978958203
