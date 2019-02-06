from API_webHMI import *
from defs import csv_writer
from head import headers, device_adress
from connections import connection

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

    file_path1 = 'rejestry/registers.csv'
    file_path2 = 'rejestry/regList.csv'
    file_path1=file_path1.replace('/', os.sep)
    file_path2 = file_path2.replace('/', os.sep)

    try:
        os.makedirs('rejestry')
    except FileExistsError:
        pass

    print('Ilosc  rejestrów : {}'.format(len(regList)))

    csv_writer(file_path1, registers)


    regs=[104.4,105.5,106.6,205.5,206.6,204.4,207.7,304.4,305.5,306.6,404.4,405.5,402.2,403.3,406.6,504.4,505.5,506.6,604.4,605.5,602.2,603.3,606.6,710.10,703.3,705.5,709.9,708.8,707.7,704.4]

    regs_string=[str(x) for x in regs]

    print(regs_string)
    for k,v in regList.items():
        # print(k,v)
        for x in regs_string:
            if x in v['plcname']:
                if 'Temp' in v['regtitle']:
                    print(k,',',v['plcname'])