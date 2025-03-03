import random

a = random.random()  # псевдослучайное (т.к. его можно просчитать) число от 0 до 1
print(a)

b = random.uniform(1, 4)  # вещественное число от 1 до 4
print(b)

c = random.randint(1, 4)  # целочисленное число от 1 до 4
print(c)

d = random.randrange(1, 10, 2)  # число от 1 до 10 с шагом 2
print(d)

"""
Все выше функции подчиняются равномерному закону распределения.
 
 Однако, на практике часто требуются Гауссовские случайные величины, т.е. большинство чисел будет сгенерировано в 
 диапазоне, близком к математическому ожиданию (среднее значение). Ценность этого распределения в том, что согласно ему, 
 происходят многие события в жизни (колебания цен на бирже, шумы при радиопередачах, погрешность измерений и т.п.)
 
 Для генерации таких чисел существует функция gauss(mu, sigma), где mu - мат. ожидание, sigma - среднеквадратическое
 отклонение (т.е. мера разброса относительно мат. ожидания)
"""

g = random.gauss(0, 5)
print(g)

"""Работа с последовательностями"""
lst = [4, 5, 0, -1, 10, 76, 3]

f = random.choice(lst)  # выбор случайного элемента из списка
print(f)

random.shuffle(lst)  # перемешивает список (работает только с изменяемыми типами данных)
print(lst)

h = random.sample(lst, 3)  # возвращает список из 3 неповторяющихся элементов из списка
print(h)

"""Возможность генерировать одинаковые последовательности псевдослучайных чисел при каждом новом запуске программы"""
j = [random.randint(0, 10) for i in range(20)]
print(j)  # всегда разные списки

random.seed(123)  # фиксируем зерно генерации случайных чисел
k = [random.randint(0, 10) for l in range(20)]
print(k)  # всегда одинаковая последовательность [0, 4, 1, 6, 4, 1, 0, 6, 8, 8, 5, 5, 0, 2, 2, 5, 8, 5, 3, 2]
