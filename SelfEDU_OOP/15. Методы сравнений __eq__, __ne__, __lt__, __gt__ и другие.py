"""Магические методы сравнений
__eq__() - для равенства ==
__ne__() - для неравенства !=
__lt__() - для оператора меньше <
__le__() - для оператора меньше или равно <=
__gt__() - для оператора больше >
__ge__() - для оператора больше и равно >=
"""


class Clock:
    __DAY = 86400  # число секунд в 1 дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY  # остаток от деления

    def __eq__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Операнд справа должен иметь тип int или Clock')

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc

    def __lt__(self, other):
        """По хорошему нужно вывести в отдельный метод, чтобы избежать дублирования"""
        if not isinstance(other, (int, Clock)):
            raise TypeError('Операнд справа должен иметь тип int или Clock')

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds < sc


c1 = Clock(1000)
c2 = Clock(1000)
c3 = Clock(2000)
print(c1 == c2)  # True (если бы же в классе не было __eq__, то будет False, т.е. сравнение само по себе возможно,
# но т.к. экземпляры классы разные, то и соответственно False
print(c1 == 1000)  # True (так тоже можно)
"""Если сделать оператор неравенства c1!=c2, то это тоже самое что и not(c1=c2), поэтому это будет корректно работать,
даже если в классе магический метод __ne__() не определен явно"""
print(c1 < c3)  # True
"""Если оператор больше не реализован, то будет работать, т.к. произойдет подмена, т.е. вместо c1>c2, будет c2<c1, 
а оператор меньше уже реализован. Если же метод меньше __gt__() задать явно, то разумеется будет вызван он.
Аналогично реализовываются и другие методы."""
