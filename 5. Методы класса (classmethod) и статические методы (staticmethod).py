class Vector:
    # атрибуты класса:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        """Это метод класса в этом случае работает только с атрибутами класса, но не может обращаться к локальным
        атрибутам экземпляра класса, т.к. нет ссылки self, но есть ссылка на сам класс cls"""
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        # Использование метода класса внутри __init__
        # if Vector.validate(x) and Vector.validate(y): # Эта строка и следующая идентичны, но предпочтительно исп. self
        if self.validate(x) and self.validate(y):  # т.к. при этом можно изменить название класса, способ универсальный
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        """Это статический метод класса, который не использует ни атрибуты класса, ни атрибуты экземпляра класса.
        Это независимая самостоятельная функция (квадрат нормы), объявленная внутри класса."""
        return x * x + y * y


"""Метод validate можно вызывать непосредственно через класс Vector, не создавая экземпляр класса"""
print(Vector.validate(5))  # True
"""Пример использования метода класса внутри __init__"""
v1 = Vector(1, 2)
print(v1.get_coord())  # (1, 2)
v2 = Vector(1, 200)
print(v2.get_coord())  # (0, 0)
"""Пример вызова статического метода класса. Причем его можно вызывать и внутри обычных методов класса."""
print(Vector.norm2(5, 6))  # 61
