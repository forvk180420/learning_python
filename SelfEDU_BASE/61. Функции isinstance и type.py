"""
isnstance проверяет принадлежность объекта к определенным типам данных
"""

a = 5
print(isinstance(a, int))  # True (т.к. а ссылается на целочисленный тип данных)
print(isinstance(a, float))  # False

# особенность с True
b = True
print(b, bool)  # True <class 'bool'>
print(b, int)  # True <class 'int'>
# в обоих случаях True, т.к. bool наследуется из int

"Строгая проверка"
print(type(b) == bool)  # True
print(type(b) == int)  # False
print(type(b) is bool)  # True (is и == - то же самое)

# можно испольовать проверку на несколько типов
print(type(b) in (bool, float, str))  # True

"""В отличие от type, isnstance делает проверку с учетмо иерархии наследования объектов"""

"""Пример. В кортеже посчитать сумму только вещественных чисел"""
data = (4.5, 8.7, True, 'book', 8, 10, -11, [True, False])

s = 0
for x in data:
    if isinstance(x, float):
        s += x
print(s)  # 13.2

"""Можно реализовать проще с помощью filter"""
s2 = sum(filter(lambda x: isinstance(x, float), data))  # (если здесь будем использовать int, то будет в итоге 8,
# т.к. True посчитается как 1 из-за наследования из int
print(s2)  # 13.2

s3 = sum(filter(lambda x: type(x) is int, data))
print(s3)  # 7
