print()  # скобки для активизации функции. Скобки - это оператор вызова функции. Само имя print - ссылка на функцию
f = print
f('hi')  # hi (вызов через ссылку)
"""Функции удобны для повторяющихся задач. 
Концепция DRY - Don't Repeat Yuorself (не повторяйся).
Имя функции принято задавать глаголом"""


def send_mail():
    text = 'Привет!'
    print(text)


send_mail()  # вызов фунцкии. Должно быть 2 отступа от функции (PEP8). Только после объявления функции.


def send(text):  # text - это параметр
    print(text)


send(text='My name')  # My name - аргумент


def print_name_old(name, old):
    print(f'Name: {name}, old: {old}')


print_name_old('Richard', 38)  # Name: Richard, old: 38
