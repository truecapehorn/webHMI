from API_webHMI import *
from defs import csv_writer
from head import headers, device_adress
from connections import connection
import csv

import os

# req2=[]

regList = {}


def request():
    print('\n2 :Registers Req\n')
    # displayHeader(headers)  # wystarczy podstawowy naglowek
    req2 = registerList(device_adress, headers)  # odczytanie listy rejestrow
    return req2


registers = request()

# Stworzenie krótrzego  slownika rejestrow z nazwami połaczen.
for r in registers:
    if r['plcid'] in connection.keys():  # uwzglednia tylko wlaczone polaczenia
        regList[r['id']] = {'plcid': r['plcid'], 'plcname': connection[r['plcid']]['dev'], 'regtitle': r['title'],
                            'category': connection[r['plcid']]['category']}

if __name__ == '__main__':
    # # key_set = set()
    # dict_list = list()

    file_path = 'rejestry/reg.csv'
    file_path=file_path.replace('/', os.sep)

    try:
        os.makedirs('rejestry')
    except FileExistsError:
        pass

    print('Ilosc  rejestrów : {}'.format(len(regList)))

    for i in registers[0:10]:
        print(i)

    csv_writer(file_path, registers)
