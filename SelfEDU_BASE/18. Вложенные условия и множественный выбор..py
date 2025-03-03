x = 11
if x % 2 == 0:
    if 0 <= x <= 9:
        print('x - цифра')
    else:
        print('x - число')
else:
    print('x - нечетное число')

"""Наибольшее из 3 чисел"""
a = 1
b = 2
c = 3
if a > b:
    if a > c:
        print('a=max')
    else:
        print('c=max')
else:
    if b > c:
        print('b = max')
    else:
        print('c = max')

"""Множественный выбор (elif = else if), взаимо исключающие проверки"""
item = int(input())

if item == 1:
    print('1')
elif item == 2:
    print('2')
elif item == 3:
    print('3')
elif item == 4:
    print('4')
else:
    print('Неверный пункт')
