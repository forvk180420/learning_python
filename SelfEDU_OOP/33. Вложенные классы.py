"""Классический пример применения вложенных классов - это описание моделей для FrameWork Django.
Используется только для удобства.
Из внешнего класса во внутренний (вниз) обращаться можно, а наоборот (вверх) нельзя, по крайней мере это не принято, а
если всё же нужно обратиться к свойству класса Women, то это можно сделать  из __init__ Meta"""


class Women:
    title = 'объект класса для поля title'
    photo = 'объект класса для поля photo'
    ordering = 'объект класса для поля ordering'

    def __init__(self, user, psw):
        self._user = user
        self._pws = psw
        self.meta = self.Meta(user + '@' + psw)

    class Meta:
        """Это вложенный класс, например для сортировки таблицы по полю id
        Это полезно, если есть одинаковые атрибуты для разных задач (ordering в данном случае)"""
        ordering = ['id']

        def __init__(self, access):
            self._access = access


print(Women.ordering)  # объект класса для поля ordering
print(Women.Meta.ordering)  # ['id']

w = Women('root', '12345')  # создается экземпляр класса Women, но не экземпляр класса Meta.
# В нашем случае он всё же создается, т.к. мы явно его создаем в инициализаторе
print(w.__dict__)  # {'_user': 'root', '_pws': '12345', 'meta': <__main__.Women.Meta object at 0x00000181BE3C65C0>}
print(w.meta.__dict__)  # {'_access': 'root@12345'}
