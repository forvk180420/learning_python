"""
Итератор - это некий интерфейс для перебора элементов любого итерируемого объекта
__iter__(self) - получение итератора для перебора объекта
__next__(self) - переход к следующему значению и его считывание
С помощью этих методов можно превратить класс в итерируемый объект, а также указать внутри явно логику работы
"""
print(list(range(5)))  # [0, 1, 2, 3, 4]
a = iter(range(5))
print(next(a))  # 0
print(next(a))  # 1 и т.д., пока не вызовется исключение StopIteration


class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        """Сам объект является итератором"""
        self.value = self.start - self.step
        return self

    def __next__(self):
        """Для получения текущего значения последовательности (self.value)"""
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


print('fr')
fr = FRange(0, 2, 0.5)
"Объект fr выступает в роли итератора"
# print(fr.__next__())  # 0.0 или print(next(fr))
# print(fr.__next__())  # 0.5
# print(fr.__next__())  # 1.0
# print(fr.__next__())  # 1.5

"Функция не может применена к объекту fr, если магический метод __iter__ не задан явно"
it = iter(fr)
for x in fr:
    print(x)  # перебор значений...


class FRange2D:
    """Формирование таблицы значений. """

    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr2d = FRange2D(0, 2, 0.5, 4)
for row in fr2d:
    for x in row:
        print(x, end=' ')
    print()

# 0.0 0.5 1.0 1.5
# 0.0 0.5 1.0 1.5
# 0.0 0.5 1.0 1.5
# 0.0 0.5 1.0 1.5
