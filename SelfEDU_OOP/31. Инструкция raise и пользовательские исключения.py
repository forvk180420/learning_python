"""
raise - генерирует исключение

raise ZeroDivisionError('Сообщение')
raise Exception('123')
raise 'Исключение'
"""

"""Можно сделать свой класс исключений, наследуемый от базового Exception"""


class MyException(Exception):
    """Если класс исключения пустой, то обычно пишут здесь для чего это сделано"""


class MyException2(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка из MyException2: {self.message}'


class PrintData:
    def send_data(self):
        raise MyException('Сработало собственное исключение')

    def send_data2(self):
        raise MyException2('сообщение ошибки из send_data2')


p = PrintData()
try:
    p.send_data()
except MyException:
    print('send_data_error')

"""Сообщение об ошибке передалось в собственный класс ошибок"""
p2 = PrintData()
p2.send_data2()  # __main__.MyException2: Ошибка из MyException2: сообщение ошибки из send_data2
