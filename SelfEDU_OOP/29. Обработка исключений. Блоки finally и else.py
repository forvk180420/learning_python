try:
    x = int(input())
    res = 5 / x
    print(res)
except ZeroDivisionError as z:  # z - ссылка на ZeroDivisionError
    print('Деление на 0')
    print(z)
else:
    print('Блок else выполняется, если ошибок не произошло')
finally:
    print('Блок finally выполняется всегда')

""" 
finally - классический пример применения: в try открыли файл, а в finally закрыли, вне зависимости от ошибок.
Также в случае применения try в функциях, finally выполняется до return.
Try/except может быть вложенным в другой Try/except
"""
