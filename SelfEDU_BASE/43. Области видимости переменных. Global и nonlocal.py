"""
При создании фалйа myprogram.py автоматически создается пространство имен.
Переменные в этом пространстве имен называются глобальными и доступны в любом месте программы.
Функция содает свое пространство имен.
nonlocal определяет значение переменной из внешней области видимости, которая в свою очередь тоже является локальной.
"""

N = 100  # глобальная переменная


def my_func(lst):
    "Функция содает свое пространство имен. lst, x, n - локальные переменные, т.е. они существуют только внутри функции"
    # N = 20  # строка никак не влияет на глобальную переменную N
    "если есть необходимость работать с глобальной переменной N, то необходимо указать global"
    global N
    N = 20
    for x in lst:
        n = x + 1 + N
        print(n)


my_func([1, 2, 3])  # 2 3 4
print(N)  # 20 (global N)

x = 0


def outer():
    x = 1

    def inner():
        nonlocal x  # будет взят x из outer
        x = 2
        print('inner: ', x)

    inner()
    print('outer: ', x)


outer()  # inner:  2 outer: 2
print('global: ', x)  # 1 global:  0
