def get_list():
    for x in [1, 2, 3, 4]:
        return x


a = get_list()
print(a)  # 1 - возвращено 1 значение и функция завершает работу


def get_list2():
    for x in [1, 2, 3, 4]:
        yield x  # получилась функция-генератор


b = get_list2()
print(b)  # <generator object get_list2 at 0x000001917B629B60>

"Перебирать можно при помощи оператора next"
print(next(b))  # 1
print(next(b))  # 2
print(next(b))  # 3
print(next(b))  # 4

"""
Оператор yield возвращает текущее значение x, замораживает состояни функции до следующего вызова next.
yield превращает любую функцию в функцию-генератор.
"""

