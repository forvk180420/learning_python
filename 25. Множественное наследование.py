"""
Пример множественного наследования - миксины (mixins, примеси).
"""


class Goods:
    def __init__(self, name, weight, price):
        # super().__init__()
        print('init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    """Это миксин, вспомогательный класс"""

    def __init__(self):
        super().__init__()  # Обращение к MixinLog2, т.к. NoteBook(Goods, MixinLog, MixinLog2)
        print('init Mixing')

    def sell_log(self):
        print(f'Товар был продан')

    def print_info(self):
        print(f'print_info из MixinLog')


class MixinLog2:
    def __init__(self):
        super().__init__()
        print('init Mixing2')


class NoteBook(Goods, MixinLog, MixinLog2):
    pass


n = NoteBook('Acer', 1, 30000)
# init Mixing
# init Goods

"""
Если в базовом классе Goods нет super().__init__(), т.е. ссылки на базовый класс Mixing не будет, а значит __init__ для 
Mixing не будет вызван, т.к. уже он был найден и вызван в Goods. Но, почему идет ссылка на Mixing, а не на самый базовый
класс object? Дело в том, что при в NoteBook(Goods, MixinLog) наследование будет идти сначала от Goods, затем от 
MixinLog и т.д.
"""
print(NoteBook.__mro__)  # (<class '__main__.NoteBook'>, <class '__main__.Goods'>, <class '__main__.MixinLog'>,
# <class 'object'>) - это порядок наследования MRO

"""
MRO - Method Resolution Order - алгоритм обхода базовых классов при множественном наследовании.
Структуру классов нужно продумывать так, чтобы вспомогательные классы не принимали никаких аргументов, иначе это 
усложнит работу с классами.
"""

"""
Вызов методов с одинаковыми именами в базовых классах
"""
n.print_info()  # вызван метод из Goods, хотя в классе MixinLog он тоже есть.
"Чтобы вызвать метод print_info() именно из MixinLog:"
MixinLog.print_info(n)  # print_info из MixinLog
"Если нужно всегда вызывать print_info() из MixinLog, то:"


class NoteBook2(Goods, MixinLog):
    def print_info(self):
        """Определяем явно вызов print_info из MixinLog"""
        MixinLog.print_info(n)


n2 = NoteBook2('Samsung', 2, 50000)
n2.print_info()  # print_info из MixinLog, а не print_info из Goods
