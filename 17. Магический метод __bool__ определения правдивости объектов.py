"""
__len__() - вызывается функцией bool(), если не определен магический метод __bool__()
__bool__() - вызывается в приоритетном порядке функцией bool()

Функция bool() возвращает True для любого значения, отличного от 0.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__')
        return self.x + self.y

    def __bool__(self):
        """Метод обязательно возвращает булево значение"""
        return self.x == self.y


p = Point(3, 4)
print(len(p))  # 7
print(bool(p))  # False, если __bool__ явно определен
"""Сначала вызывается __bool__, если магический метод задан явно, если нет, то __len__ (если задан явно).
Применяется при неявном вызове функции bool():
"""
if p:
    print('p True')
else:
    print('p False')

