"""
if - условный оператор (оператор ветвления)
"""
# При отладке построчный переход: Step Over (F8)

x = -4
if x < 0:
    x = -x
print(x)  # 4

a = float(input('a:'))
b = float(input('b:'))
if a < b:
    a, b = b, a
print(a, b)

if a:  # Любое значение, кроме нуля выполняется условие
    print('a True')

"""Условия для списков"""
marks = [3, 3, 4, 2, 4]

if 2 in marks:
    print('студент будет отчислен')
else:
    print('OK')
