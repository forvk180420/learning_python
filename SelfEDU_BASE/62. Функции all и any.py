"""
ALL
Пример. Узнать, принимают ли все элементы списка значения True.

ANY

"""
a = [True, True, True, True]

b = all(a)
print(b)  # True

c = [True, False, True, True]  # если хотя бы 1 элемент False -> False
d = all(c)
print(d)  # False

"""
Принцип работы. Каждый элемент списка итерируется по функции bool и возвращает True или False.
"""
e = [0, 1, 2.5, '', 'python', [], [1, 2], {}]
f = all(e)
print(f)  # False

"""Теперь изменим список, чтобы применяемая функция bool возвращала True для каждого элмента"""
g = [1, 2.5, 'python', [1, 2]]
h = all(g)
print(h)  # True

"ANY (Возвращает True, если встретилось хотя бы 1 значение True)"
print('---ANY---')
print(any(a))  # True
print(any([False, False, 0]))  # False
print(any([False, False, 0, 1]))  # True

