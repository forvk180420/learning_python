"""FrameWork Django использует метаклассы для связи объектов с записями в БД, т.е. для реализации API.
Можно определить некий класс модели с набором атрибутов, причем эти атрибуты совпадают с полями таблицы БД
Название атрибута = название столбца в БД
"""


class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        """Фактически это инициализатор класса Women"""
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = 'Заголовок'
    content = 'Контент'
    photo = 'Путь к фото'


w = Women()
print(w.__dict__)  # {'__module__': '__main__', '__qualname__': 'Women', 'title': 'Заголовок', 'content': 'Контент',
# 'photo': 'Путь к фото'}

"""Класс Women можно реализовать таким образом (это будет эквивалентно записи выше):"""


class Women2:
    class_attrs = {'title': 'заголовок', 'content': 'контент', 'photo': 'путь к фото'}
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'

    def __init__(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value


"""Мы прописываем модель на простом уровне class Women, а далее добавляется необходимый функционал, чтобы в экземплярах
класса модели у нас появлялись необходимые данные, уже взятые из таблицы БД, т.е. это элемент реализации API ORM Django
"""
