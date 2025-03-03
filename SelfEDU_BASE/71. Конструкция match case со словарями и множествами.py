"Словари"
request = {'url': 'yandex.ru', 'method': 'GET', 'timeout': 1000}

match request:
    case {'url': url, 'method': method, 'timeout': timeout} if timeout < 500:
        print('<500')
    case {'url': url, 'method': method}:  # шаблон отрабатывает, если на входе словарь и он имеет url и method
        # наличие или отсутствие ключей в исходном словаре не важно
        # можно добавить проверку на тип данных:
        # case {'url': str() as url, 'method': method}:
        print(f'Запрос: url: {url}, method: {method}')
    case {'url': url, 'method': method, 'timeout': 1000 | 2000}:
        print('1000 | 2000')
    case {'url': url, 'method': method, **kwargs} if len(
            kwargs) <= 2:  # проверка, что других ключей в словаре не более 2
        print('len(kwargs)<=2')
    case {'url': url, 'method': method, **kwargs} if not kwargs:  # проверка, что других ключей в словаре нет
        print('len(kwargs)<=2')
    case _:
        print('неверный запрос')

json_data = {'id': 2, 'type': 'list', 'data': [1, 2, 3], 'access': True, 'date': '01.01.2023'}

match json_data:
    case {'type': 'list', 'data': data}:
        print('Проверка, если тип - лист, то получить данные')

json_data2 = {'id': 2, 'access': True, 'info': ['01.01.2023', {'login': '123', 'email': 'email@m.ru'}, True, 1000]}

match json_data2:
    case {'access': True, 'info': [_, {'email': email}, _, _]}:  # _ - нужно учесть порядок значений в упорядочных
        # коллекциях при распаковке
        print(f'Проверка, если есть доступ, то из блока info извлечь email {email}')

"Множества"
primary_keys = {1, 2, 3}

match primary_keys:
    case set() as keys if len(keys) == 3:
        print('Проверка, если это множество и количество элементов в нем равно 3')
    case _:
        print('Исключение')
