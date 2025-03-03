def print_text(name, old):
    text = f'Привет, {name}! Твой возраст: {old}'
    print(text)


def get_sqrt(x):
    """Вычисление квадратного корня"""
    res = None if x < 0 else x ** 0.5  # переменная res существует только внутри функции
    return res  # на этом месте функция заврешает работу
    # return x - возврата x не будет, т.к. функция завершена выше


a = get_sqrt(49)  # 49 это аргумент
print(a)  # 7.0


def get_max2(a, b):
    return a if a > b else b


"""определим наибольшее из 2 чисел"""
x, y = 5, 7
print(get_max2(x, y))  # 7

"""определим наибольшее из 3 чисел"""
q, w, e = 4, 6, 8
print(get_max2(q, get_max2(w, e)))  # 8 . Сначала будет выполнена функция, которая задана в качестве аргумента


def get_max3(a, b, c):  # Вызов функции из другой функции (функциональный подход)
    return get_max2(a, get_max2(b, c))


print(get_max3(a=1, b=2, c=3))  # 3

"""Выведем четные числа из диапазона (пример использования)"""

print('-' * 10)


def even(x):
    return x % 2 == 0


for i in range(1, 10):
    if even(i):
        print(i)  # 2 4 6 8
