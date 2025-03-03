# file = open('my_file.txt', 'w')  # w = открытие на запись (все его содержимое до этого уничтожается
# file.write('hi')
# file.close()

try:
    with open('out.txt', 'w') as file:
        file.write('hi')
except:
    print('Error')

"""
a = append (добавить) - данныее будут добавляться
w = открытие на запись (все его содержимое до этого уничтожается
r = read - данные будут только считываться. 
b = бинарный режим

Мы не можем считать данные, если файл открыт на запись или дозапись.
a+ = можно считывать и записывать

Есть еще БИНАРНЫЙ РЕЖИМ РАБОТЫ - данные из файла считываются один в один без какой-либо обработки.
"""

import pickle

books = [('Евгений Онегин', 'Пушкин А.С.', 200), ('Муму', 'Тургенев И.С.', 250)]

file = open('books.bin', 'wb')  #
pickle.dump(books, file)
file.close()

file2 = open('books.bin', 'rb')
bs = pickle.load(file2)
file.close()
print(bs)  # [('Евгений Онегин', 'Пушкин А.С.', 200), ('Муму', 'Тургенев И.С.', 250)]

"""
Работа с несколькими коллекциями (блоками). Сохраним их все в 1 файл
"""
book1 = ['Евгений Онегин', 'Пушкин А.С.', 200]
book2 = ['Муму', 'Тургенев И.С.', 250]
"Запись"
try:
    with open('blocks2.bin', 'wb') as file3:
        pickle.dump(book1, file3)
        pickle.dump(book2, file3)
except:
    print('Ошибка при работе с файлом')
"Чтение"
try:
    with open('blocks2.bin', 'rb') as file4:
        b1 = pickle.load(file4)
        b2 = pickle.load(file4)
except:
    print('Ошибка при работе с файлом')

print(b1, b2)
