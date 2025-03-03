"""
__getitem__(self, item) - получение значения по ключу item
__setitem__(self, key, value) - запись значения value по ключу key
__delitem__(self, key) - удаление элемента по ключу key
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Индекс должен быть целым неотрицательным числом')
        if key >= len(self.marks):
            "Если значение key больше длины списка, то будет исключение. Чтобы эот исправить:"
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)  # Расширяем размер списка до нужного размера key
        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Индекс должен быть целым неотрицательным числом')
        del self.marks[key]


s1 = Student('Сергей', [5, 5, 3, 2, 5])
"Для получения значения из заданной коллекции используется магический метод __getitem__"
print(s1[2])  # 3 \Потому как магический метод __getitem__ задан явно, иначе исключение
"Для изменения значения заданной коллекции используется магический метод __setitem__"
s1[2] = 4
print(s1[2])  # 4 или также print(s1.marks[2])
"Пример, когда значение key больше длины списка"
s1[10] = 5
print(s1.marks)  # [5, 5, 4, 2, 5, None, None, None, None, None, 5]
"Для удаления значения из заданной коллекции используется магический метод __delitem__"
del s1[10]
print(s1.marks)  # [5, 5, 4, 2, 5, None, None, None, None, None]
