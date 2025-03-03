def say_name(name):
    def say_goodbye():
        print(f'Goodbye, {name}!')

    say_goodbye()


say_name(name='Max')  # Goodbye, Max!

"Если мы функцию say_goodbye не будем вызывать, но возвратим ее, то print не будет выполнен, т.к. она не вызывается." \
"Но, мы можем сохранить ссылку на нее - f. А затем вызвать ее через ссылку - f()"


def say_name(name):
    def say_goodbye():
        print(f'Goodbye, {name}!')

    return say_goodbye


f = say_name(name='Max')  # Goodbye, Max!
f()  # Goodbye, Max!
"Откуда функция say_goodbye берет внешнюю переменную name?" \
"Это из-за того, что внешнее окружение не удаляется, а продолжает существовать. " \
"У каждого локального окружения есть неявная (скрытая) ссылка на внешнее окружение." \
"В данном случае say_goodbye -> say_name -> на глобальное внешнее окружение (glob)." \
"Такой эффект, когда мы держим эти внутренние локальные окружения и имеем возможность использовать переменные из " \
"внешних окружений, называется ЗАМЫКАНИЕМ. Замыкания в том смысле, что мы держим внутренние окружения как бы по " \
"цепочке, т.е. у нас получается замыкающаяся цепочка ссылок: f()->say_goodbye()->say_name->glob->f()" \
"При этом при каждом новом вызове: f2(), f3() будет создаваться свое независимое локальное окружение (разные name)."
f2 = say_name(name='Python')
f2()  # Goodbye, Python!

"""
ПРИМЕР использования: счетчик. 
"""


def counter(start=0):
    def step():
        nonlocal start  # Чтобы использовать переменную start из внешнего окружения.
        start += 1
        return start

    return step


c1 = counter(start=10)
c2 = counter()
print(c1(), c1(), c1())  # 11 12 13
print(c2(), c2(), c2())  # 1 2 3
"Все счетчики выше работают независимо друг от друга, благодаря замыканию"

"""
ПРИМЕР использования: функция, которая будет удалять определенные символы в начале и в конце строки. 
"""


def strip_string(strip_chars=' '):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


strip1 = strip_string()
strip2 = strip_string(" !?,.;")

print(strip1(string=' Hi, Python!.. '))  # Hi, Python!..
print(strip2(string=' Hi, Python!.. '))  # Hi, Python
