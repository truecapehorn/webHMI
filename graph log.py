from reqesty_webHMI import *


def displayHeader(dic):
    print('\nHeader')
    for k, v in dic.items():
        print(k, ':', v)


def displayList(list):
    print('\nLista')
    for i in list:
        print(i)


def makeRegHeader(ids):
    regs = ''
    for i in ids:
        regs = regs + i + ','
    regs = regs[:-1]
    return regs


# USER = 'admin'
# PASS = 'elam4321'
device_adress = 'http://80.50.4.62:60043'

'''
headers = {'X-WH-APIKEY': 'D606230FEB2CCF4A3520B334BE0E5A29C1311EB0',
           'Accept': 'application/json',
           'Content-Type': 'application/json',
           'X-WH-CONNS': '1,2,3,4,5',
           'X-WH-START': '1546819261',
           'X-WH-END': '1547123883',
           'X-WH-REG-IDS': '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16',
           'X-WH-SLICES': '400',
           'X-WH-REGS': '1,2,3,4',
           }
'''

headers = {'X-WH-APIKEY': 'D606230FEB2CCF4A3520B334BE0E5A29C1311EB0',
                 'Accept': 'application/json',
                 'Content-Type': 'application/json',

                 'X-WH-CONNS': '',
                 'X-WH-START': '',
                 'X-WH-END': '',
                 'X-WH-REG-IDS': '',
                 'X-WH-SLICES': '',
                 'X-WH-REGS': '',

                 }

connection = {}
appars=[]
fifs=[]
conns = []
devs = []
graphs_humidity = []
graphs_temperature = []
graphs_data = []

print('\nConnection Req')
displayHeader(headers)
req1 = connectionList(device_adress, headers)
for i in req1:
    connection[i['id']] = i['title']
print('Ilość połaczen : {}'.format(len(connection)))

for k, v in connection.items():
    if v[0:3]=='APA' :
        appars.append(k)  # apary
    elif v[0:3]=='FIF' :
        fifs.append(k)  # fify

print('Ilosc Aparow: {}'.format(len(appars)))
print(appars)
print('Ilosc Fifow: {}'.format(len(fifs)))
print(fifs)

# Ustalenie nagłowka dla listy rejestrow

print('\nRegisters Req')
displayHeader(headers)
req2 = registerList(device_adress, headers)  # odczytanie listy rejestrow
print('Lista rejestrów : {}'.format(len(req2)))
print(req2[0])

# Ustalenie jakie rejstry mają wykresy
for i in req2:
    if i['plcid'] in fifs:
        if i['save_graph_data'] == '1' and i['measureUnits'] == '%RH':
            graphs_humidity.append(i['id'])  # dla wilgotnosci
        elif i['save_graph_data'] == '1' and i['measureUnits'] == '°C':
            graphs_temperature.append(i['id'])  # dla temperatury

print('Ilosc rejestrow wilgotnosci z wykresami: {}'.format(len(graphs_humidity)))
print(graphs_humidity)

print('Ilosc rejestrow temperatury wykresami: {}'.format(len(graphs_temperature)))
print(graphs_temperature)

# Pobranie wykresow

print('\nDane z wykresow')
wh_start = 1546819261  # start dla wykresu
wh_stop = wh_start + 60 * 60  # 24 h
wh_slices = 4  # minimlana ilosc czesci

# Ustalenie nagłowka dla wykresu
headers['X-WH-CONNS']=''
headers['X-WH-REGS'] = makeRegHeader(appars)
headers['X-WH-START'] = str(wh_start)
headers['X-WH-END'] = str(wh_stop)
headers['X-WH-SLICES'] = str(wh_slices)
displayHeader(headers)
# req3 = getGraphData(device_adress, headers)
#
# log = open('graphs.txt', 'w')
# print(req3, file=log)
# log.close()
