"""
Полиморфизм - это возможность работы с совершенно разными объектами (языка Python) единым образом, т.е. через единый
интерфейс.
"""


class Geom:
    def get_pr(self):
        raise NotImplementedError('В дочернем классе должен быть переопределен метод get_pr()')


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    # def get_rect_pr(self):
    #     return 2 * (self.w + self.h)

    # def get_pr(self):
    #     return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_pr(self):
        return 4 * self.a

    def get_pr(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def get_tr_pr(self):
    #     return self.a + self.b + self.c

    def get_pr(self):
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

print(s1.get_sq_pr(), s2.get_sq_pr())  # 40 80
print('-' * 30)
"""Если записать все объекты в виде списка geom и вызвать метод для получения периметра, то будет ошибка, т.к. названия
методов в каждом из классов разные (get_rect_pr, get_sq_pr, get_tr_pr). Можно сделать проверку для каждого класса, но, 
это не лучшая реализация. Теперь нужно во всех классах обозначить метод получения периметра одинаково: get_pr

for g in geom:
    print(g.get_sq_pr())
"""
geom = [r1, r2, s1, s2, t1, t2]

"""После того, как мы убедились, что во всех классах присутствует метод get_pr, можно реализовать перебор:"""

for g in geom:
    print(g.get_pr())  # NotImplementedError: В дочернем классе должен быть переопределен метод get_pr()

"""
Это и есть пример полиморфизма, когда к разным объектам можно обращаться через единый интерфейс, в данном случае: get_pr
Если в классе нет get_pr, то для него можно сделать базовый класс с методом get_pr с заглушкой исключения, о том, что 
нет метода get_pr в дочернем классе.

Методы, которые обязательно нужно переопределять в дочерних классах и которые не имеют своей собственной реализации,
называются АБСТРАКТНЫМИ (в питоне абстракция имитационная, т.к. явно формируется исключение для переопределения 
NotImplementedError).
"""
