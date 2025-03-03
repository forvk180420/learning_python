"""Вычислить факториал натурального числа n"""
n = int(input('Введите n до 100: '))

if n < 1 or n > 100:
    print('Число вне диапазона!')
else:
    p = 1
    for i in range(1, n + 1):
        p *= i

    print(f'{n}!={p}')

"""Заменить все двузначные числа нулями"""

digs = [4, 3, 100, -53, -30, 1, 34, -8]

for i in range(len(digs)):
    if 10 <= abs(digs[i]) <= 99:
        digs[i] = 0
print(digs)

"""Заменить все двузначные числа нулями c enumerate"""

for i, d in enumerate(digs):
    print(f'i = {i}, d = {d}')  # i = 0, d = 4 , i = 1, d = 3 ...
    if 10 <= abs(d) <= 99:
        digs[i] = 0
print(digs)

"""Перевод Кириллицы в Латиницу"""

start_index = ord('a')  # значение кода
print(start_index)
