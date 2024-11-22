"""
В случае многопоточного процесса, когда в каждом потоке создается свой экземпляр класса может возникнуть необходимость,
чтобы все экземпляры имели единые (общие для всех экземпляров) локальные свойства и изменение любого из свойств внутри
какого-либо экземпляра, отражалось бы и в других экземплярах. Это паттерн МОНОСОСТОЯНИЕ.
"""


class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs  # __dict__ хранит локальные свойства экземпляра класса


pt1 = ThreadData()
pt2 = ThreadData()

# во всех экземплярах класса значение id одинаково изначально
print(pt1.id)  # 1
print(pt1.id)  # 1

# При изменении значения свойства id в одном экземпляре меняются значения и во всех других экземплярах
pt1.id = 2
print(pt1.id)  # 2
print(pt1.id)  # 2

# При добавлении нового свойства в один экземпляр класса, оно появляется и во всех остальных
pt1.attr_new = 'new_attr'
print(pt1.attr_new)  # new_attr
print(pt2.attr_new)  # new_attr
