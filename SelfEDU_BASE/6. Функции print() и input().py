"""
print()
"""
a = 1
b = 2
c = 3
"""Добавление разделителя"""
print(a, b, c, sep=';')  # 1;2;3
"""Добавление завершающего символа"""
print('Hello', end=' ')
print('World')  # Hello World (1 строка)

"""
input()
"""
a = input('Введите A:')
print(a, type(a))

"""Ввод значений через пробел"""
a, b = map(float, input("Ввведите через пробел A и B:").split())
print(f'A = {a}, B = {b}')
