"""Магические методы арифметических операций
__add__() - для операции сложения
__sub__() - для операции вычитания
__mul__() - для операции умножения
__truediv__() - для операции деления
"""


class Clock:
    __DAY = 86400  # число секунд в 1 дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY  # остаток от деления

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        """Возвращаем новый экземпляр класса, который будет содержать новое значения секунд"""
        if isinstance(other, Clock):
            """Эта проверка нужна, если есть необходимость суммировать экземпляры класса (с3 = c1 + c2)"""
            other = other.seconds
        return Clock(self.seconds + other)

    def __radd__(self, other):
        """Если экземпляр класса будет справа от оператора сложения (с1 = 100 + с1)"""
        return self + other  # после выполнения этой строки запускается __add__

    def __iadd__(self, other):
        """Для корректной обработки записи вида: c1 += 100"""
        if isinstance(other, Clock):
            other = other.seconds
        self.seconds += other
        return self


c1 = Clock(1000)
print(c1.get_time())  # 00:16:40
"Для того, чтобы увеличить количество секунд уже в созданном экземпляре класса нужно:"
c1.seconds = c1.seconds + 100
print(c1.get_time())  # 00:18:20
"""Чтобы упростить запись и не обращаться к локальному свойству seconds, можно c1 = c1 + 100, но, 
для этого нужен магический метод __add__"""
c1 = c1 + 100  # в действительности вызывается: c1.__add__(100)
print(c1.get_time())  # 00:20:00

c2 = Clock(2000)
c3 = c1 + c2
print(c3.get_time())  # 00:53:20
