"""
Для обработки исключений FileNotFoundError
"""
try:
    file_ = open('my_file.txt', encoding='utf-8')
    with open('my_file.txt', encoding='utf-8') as file:  # менеджер контекста, заменяет код ниже, автоматически закроет
        s = file.readlines()
        print(s)
# try:
#     s = file.readlines()
#     print(s)
# finally:
#     file.close()
except FileNotFoundError:
    print('Невозможно открыть файл')
except:
    print('Ошибка при работе с файлов')
finally:
    print(file.closed)  # True (файл закрыт)
