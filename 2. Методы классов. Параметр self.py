"""
В названиях методов обычно используются глаголы, а в названиях свойств - существительные
"""


class Point:
    "Класс для представления координат точек на плоскости"
    color = 'red'  # переменные внутри класса - это его атрибуты или свойства
    circle = 2

    def set_exmp(sefl):  # self - ссылка на экземпляр класса
        print('вызов метода set_coords')
        print(str(sefl))

    def set_coords(sefl, x, y):  # self - ссылка на экземпляр класса
        sefl.x = x  # Создаем 2 локальных свойства
        sefl.y = y


pt = Point()
pt.set_exmp()  # вызов метода set_coords \n<__main__.Point object at 0x000001DAE4A30EB0>
pt.set_coords(x=1, y=2)
print(pt.__dict__)  # {'x': 1, 'y': 2}

"Получаемые координаты x и y совершенно независимы в разных экземплярах класса"
pt2 = Point()
pt2.set_coords(x=10, y=20)
print(pt2.__dict__)  # {'x': 10, 'y': 20}
