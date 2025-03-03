"""
break - досрочно завершает цикл
continue - пропускает 1 итерацию цикла
"""
print('Запуск цикла')
i = 0
while True:
    i += 1
    break

print('Завершение цикла')

"""Найти хотя бы одно четное значение"""
d = [1, 5, 3, 6, 0, -4]
flagFind = False
while i < len(d):
    print(i)
    flagFind = d[i] % 2 == 0
    if flagFind:
        break
    i += 1
print(flagFind)  # True

# """continue
# вводим числа с клавиатуры, нечетные суммируем, при нуле останавливаем"""
# s = 0
# g = 1
# while g != 0:
#     g = int(input('Введите целое число:'))
#     if g % 2 == 0:
#         continue
#     s += g
#     print(f's = {s}')

"""else"""
# S = 1/2+1/3+1/4+...+1/0

S = 0
I = -10

while I < 0:
    if I == 0:
        break
    S += 1 / I
    I += 1
else:
    print('Сумма вычислена корретно')

print(S)
