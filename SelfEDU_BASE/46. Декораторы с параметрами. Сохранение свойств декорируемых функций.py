import math


def df_decorator(dx=0.01):  # добавляем ещё одну внешнюю функцию для того, чтобы при вызове декоратора можно указать
    # дополнительные параметры
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            "Вычисляем производную функции"
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        return wrapper

    return func_decorator


@df_decorator(dx=0.001)
def sin_df(x):
    return math.sin(x)


df = sin_df(math.pi / 3)
print(df)

