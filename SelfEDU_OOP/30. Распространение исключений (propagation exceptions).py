def func2():
    return 1 / 0


def func1():
    return func2()


print('1')
print('2')
func1()
print('3')

"""
1
2
Traceback (most recent call last):
  File "F:\PycharmProjects\SelfEDU_OOP\30. Распространение исключений (propagation exceptions).py", line 11, in <module>
    func1()
  File "F:\PycharmProjects\SelfEDU_OOP\30. Распространение исключений (propagation exceptions).py", line 6, in func1
    return func2()
  File "F:\PycharmProjects\SelfEDU_OOP\30. Распространение исключений (propagation exceptions).py", line 2, in func2
    return 1 / 0
ZeroDivisionError: division by zero

Таким образом можно отследить весь стек ошибок. Ставить обработку исключений можно на любом уровне, в этом случае код
прерываться не будет.
"""
