import time


def get_nod(a, b):
    """
    Вычисляется НОД по алгоритму Евклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def test_nod(func):  # func - это ссылка на функцию
    # тест №1
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('test1 - OK')
    else:
        print('test1 - FAIL')

    # test 2
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print('test2 - OK')
    else:
        print('test2 - FAIL')
    # test 3
    a = 2
    b = 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print('test3 - OK')
    else:
        print('test3 - FAIL')


test_nod(get_nod)

res = get_nod(18, 24)
print(res)  # 6
help(get_nod)  # Вывод описания


def get_nod_fast(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b

    return a


test_nod(get_nod_fast)

