from API_webHMI import *
from defs import *
from head import headers, device_adress


# connection = {}
# appars = []
# fifs = []


def request():
    print('1: Connection Req\n')
    # displayHeader(headers)
    req1 = connectionList(device_adress, headers)  # pobranie listy polaczen plc.
    return req1


def devices(req1):
    connection = {}
    appars = []
    fifs = []
    for i in req1:
        if i['disabled'] == '0':  # branie tylko pod uwage włączone polaczenia
            connection[i['id']] = {'dev': i['title'],
                                   'category': i['category']}  # utworzenie slownika dla id i nazyw polaczenia
            # connection[i['category']] = i['category']  # dodanie do slownika gdzie jest dane urzadzenie

    for k, v in connection.items():  # rozdzial na fiy i apary
        if 'APA' in v['dev']:
            appars.append(k)  # apary
        elif 'FIF' in v['dev']:
            fifs.append(k)  # fify
    return connection, appars, fifs


# req1 = request()
# conn = devices(req1)
connection, appars, fifs = devices(request())

if __name__ == '__main__':
    print('Ilość połaczen : {}'.format(len(connection.keys())))
    print(connection)
    print('Ilosc Aparow: {}'.format(len(appars)))
    print(appars)
    print('Ilosc Fifow: {}'.format(len(fifs)))
    print(fifs)
