lst: list = [1, 2, '3']  # самый простой вариант, но нет никаких аннотаций элементов списка
lst2: list[int] = [1, 2]  # список, внутри которого целочисленные значения

addr: tuple[int, str] = (1, '2')  # кортеж, указываем для каждого элемента, т.к. кортеж подразумевает группировку
elems: tuple[float, ...]  # кортеж, но все элементы float

words: dict[str, int] = {'one': 1, 'two': 2}  # словарь, указываем тип ключа и тип значения (можно и не указывать)

persons: set[str] = {'asaf', 'saffsf'}  # множество, все аналогично


def get_positive(digits: list[int]) -> list[int]:
    return list(filter(lambda x: x > 0, digits))


print(get_positive([-2, 3, 4, 5, -1]))  # [3, 4, 5] (убраны отрицательные)
