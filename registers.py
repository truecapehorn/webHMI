from API_webHMI import *
from defs import *
from head import headers, device_adress
from connections import connection

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
        regList[r['id']] = {'plcid': r['plcid'], 'plcname': connection[r['plcid']]['dev'], 'regtitle': r['title'],'category':connection[r['plcid']]['category']}

if __name__ == '__main__':

    print('Lista rejestrów : {}'.format(len(regList)))
    for k,v in sorted(regList.items()):
        print(k,v)

