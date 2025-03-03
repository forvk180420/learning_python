"""
Распаковка может быть не только с кортежами, но и с другими итерируемыми объектами.
Нельзя упаковать уже упакованные значения.
Python исходя из контекста понимает, когда происходит упаковка, а когда распаковка.
"""
x, y = (1, 2)  # x = 1, y = 2

# x, y = (1, 2, 3, 4)  # ошибка

a, *b = (1, 2, 3, 4)
print(a, b)  # 1 [2, 3, 4] (b - это список из всех остальных значений кортежа)

*a, b = (1, 2, 3, 4)
print(a, b)  # [1, 2, 3] 4

c, *d = [1, '2', True, 4]
print(c)  # 1
print(d)  # ['2', True, 4]

*c, d = 'string'
print(c)  # ['s', 't', 'r', 'i', 'n']
print(d)  # g

# *e = 1, 2, 3 #ошибка. Нельзя упаковать уже упакованные значения.

"""Задача из списка сделать кортеж методом распаковки"""
a = [1, 2, 3]
print((a,))  # ([1, 2, 3],) - получился кортеж, состоящий из 1 элемента - списка
print((*a,))  # (1, 2, 3)

d = (-5, 5)
# range(d) #ошибка
print(list(range(*d)))  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
print([*range(*d)])  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4] - * (звездочка) перед range обозначает автоматическую
# распаковку итерируемого объекта

print([*range(*d), *(True, False), *a])  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, True, False, 1, 2, 3] - единый список

f = {0: 'безнадежно', 1: 'убого', 2: 'неуд.', 3: 'удовл.', 4: 'хорошо', 5: 'отлично'}
print(*f)  # 0 1 2 3 4 5 (множество)
print(*f.values())  # безнадежно убого неуд. удовл. хорошо отлично - множество из значений
print(*f.items())  # (0, 'безнадежно') (1, 'убого') (2, 'неуд.') (3, 'удовл.') (4, 'хорошо') (5, 'отлично')
print({**f})  # {0: 'безнадежно', 1: 'убого', 2: 'неуд.', 3: 'удовл.', 4: 'хорошо', 5: 'отлично'} - распаковка словаря
# (бессмысленно в данном случае)
# но если есть другой словарь:
f2 = {6: 'превосходно', 7: 'элитарно', 8: 'божественно'}
# то эти словари можно объединить распаковкой этих словарей:
print({**f, **f2})  # {0: 'безнадежно', 1: 'убого', 2: 'неуд.', 3: 'удовл.', 4: 'хорошо', 5: 'отлично',
# 6: 'превосходно', 7: 'элитарно', 8: 'божественно'}
