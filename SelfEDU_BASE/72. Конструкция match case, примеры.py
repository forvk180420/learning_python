def connect_db(connect: dict) -> str:
    match connect:
        case {'server': host, 'login': login, 'password': psw, 'port': port}:
            return f'connection: {host}@{login}.{psw}:{port}'
        case {'server': host, 'login': login, 'password': psw}:
            # если не указывается порт, он назначается по умолчанию
            port = 22
            return f'connection: {host}@{login}.{psw}:{port}'
        case _:
            return 'error connection'
    if not (10 < port < 50):  # можно комбинировать match и if, вынося к примеру отдельно условия для порта.
        return None

    # return f'connection: {host}@{login}.{psw}:{port}' т.к. есть дублирование кода, то формирование возвращаемой строки
    # можно сделать так. Тогда в 1 case можно прописать pass (нужен как минимум 1 оператор), а во 2 case этим оператором
    # будет port = 22. Соответственно в обоих случаях следует убрать return.


request = {'server': '127.0.0.1', 'login': 'root', 'password': '1234', 'port': 24}

result = connect_db(request)
print(result)


"""Пример использования константы в match case"""
CMD_3 = 3
CMD_5 = 5
CMD_7 = 7
cmd = 5
match cmd:
    case 3: # если напрямую использовать CMD_3, то здесь будут отлавливаться все варианты, также как и с _.
        print('3')
    case x if x == CMD_5: # хитрость, чтобы использовать константу CMD_5
        print('5')
        # можно использовать константы как импортированные значения из другого модуля или класса
        # import consts
        # case consts.CMD_7:...

