"""Итерируемые объеты - объекты, состоящие из множестова елементов, которые можно перебирать"""

d = [1, 2, 3, 4, 5]
for i in d:
    print(i)  # 1 2 3 4 5
for i in [0, 1, 2, 3, 4]:
    d[i] = 0

print(d)  # [0, 0, 0, 0, 0] (изменится)

"""
Функция range()
range(start, stop, step)
range(start, stop)
range(stop)
"""

print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(0)))  # []
print(list(range(-7)))  # []
print(list(range(0, -5)))  # []
print(list(range(-10, -5)))  # [-10, -9, -8, -7, -6]
print(list(range(-10, -5, 2)))  # [-10, -8, -6]
print(list(range(-10, -5, -2)))  # []

"""находим
S = 1/2+1/3+1/4+...+1/1000
"""
S = 0
for i in range(2, 1001):
    S += 1 / i
print(S)
