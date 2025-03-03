age = 18
name = 'Сергей'

"""Привет, я Сергей. Мне 18 лет."""
print('Привет, я ' + name + '. Мне ' + str(age) + ' лет.')
print('Привет, я {0}. Мне {1} лет.'.format(name, age))
print('Привет, я {fio}. Мне {old} лет.'.format(fio=name, old=age))
print(f'Привет, я {name}. Мне {age} лет.')
