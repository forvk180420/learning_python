"""Пример разработки класса Person
ФИО (список из 3 строк, без возможности изменения), возраст (целое число от 14 до 120)"""
from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old):
        # self.verify_fio(fio)  # проверка корректности ФИО (не нужно, т.к. проверка проводится в сеттере)
        self.fio = fio  # можно писать так, а не self.__fio = fio. В этот момент вызывается геттер, в котором идет
        # проверка
        self.old = old

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')
        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER  # ascii_letters-набор маленьких и больших латинских букв
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО должен быть хотя бы один символ')
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО можно использовать только буквенные символы и дефис')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Возраст должен быть целым числом от 14 до 120')

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old


p = Person('Балакирев Сергей Михайлович', 30)
print(p.old)  # 30
p.old = 40
print(p.old)  # 40
# p2 = Person('Балакирев2 Сергей Михайлович', 30)  # TypeError: В ФИО можно использовать только
# буквенные символы и дефис
