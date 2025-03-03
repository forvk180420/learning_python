import mymodule

mymodule.floor(-5.4)

print(dir(mymodule))  # ['NAME', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__', 'floor', 'math']

a = mymodule.math.floor(-5.6)
print(a)  # -6

"Если модуль mymodule будет находиться в подкаталоге, то его явно нужно указать через точку"

"sys отображает пути, в которых происходит поиск модулей"
import sys

print(sys.path)

"Можно добавить каталог в sys, если путь до модуля особый."

sys.path.append('path_to_module')  # применяется редко

"Если модуль находится в иерархии на папку выше, то он также импортируется без ошибок. Это потому, что рабочий " \
"каталог добавляется в sys"

"""
При импорте модулей интерпретатор компилирует всю программу модуля в байт-код и выполняет его 1 раз.
"""