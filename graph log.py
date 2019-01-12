from API_webHMI import *


def displayHeader(dic):
    print('\nHeader')
    for k, v in dic.items():
        print(k, ':', v)
    print('\n')


def displayList(list):
    print('\nLista')
    for i in list:
        print(i)
    print('\n')


def makeRegIDs(ids):
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
appars = []
fifs = []
conns = []
devs = []
graphs_all = []
all_graphs_humidity = []
all_graphs_temperature = []
fif_graphs_humidity = []
fif_graphs_temperature = []
apar_graphs_humidity = []
apar_graphs_temperature = []
graphs_data = []

print('\nConnection Req')
displayHeader(headers)
req1 = connectionList(device_adress, headers)  # pobranie listy polaczen plc.

for i in req1:
    # if i['id']==str(159):
    #     print(i)
    # if i['id']==str(237):
    #     print(i)
    if i['disabled']=='0': # branie tylko pod uwage włączone polaczenia
        connection[i['id']] = i['title']  # utworzenie slownika dla id i nazyw polaczenia
print('Ilość połaczen : {}'.format(len(connection.keys())))
print(connection.keys())

for k, v in connection.items():  # rozdzial na fiy i apary
    if v[0:3] == 'APA':
        appars.append(k)  # apary
    elif v[0:3] == 'FIF':
        fifs.append(k)  # fify

print('Ilosc Aparow: {}'.format(len(appars)))
print(appars)
print('Ilosc Fifow: {}'.format(len(fifs)))
print(fifs)

print('\nRegisters Req')
displayHeader(headers)  # wystarczy podstawowy naglowek
req2 = registerList(device_adress, headers)  # odczytanie listy rejestrow
print('Lista rejestrów : {}'.format(len(req2)))
# for i in req2:
#     if i['id'] == str(648):
#         print(i) # przykladopwy ciag danych
#     if i['id']==str(3862):
#         print(i)

# Ustalenie jakie rejstry mają wykresy
# todo : Nie ma chyba sensu rozdzielac tylko na wilgotnosc i temperature.
#  Jak wywala przy sciaganiu to trzeba chyba wszystkir sciagac po koleii
for i in req2:
    if i['plcid'] in connection.keys():
        if i['save_graph_data'] == '1':
            graphs_all.append(i['id'])  # dla wszystkich ktore maja wykresy
            if i['measureUnits'] == '%RH':
                all_graphs_humidity.append(i['id'])  # dla wilgotnosci
            elif i['measureUnits'] == '°C':
                all_graphs_temperature.append(i['id'])  # dla temperatury
        if i['plcid'] in fifs: # tylko dla fifow
            if i['save_graph_data'] == '1' and i['measureUnits'] == '%RH':
                fif_graphs_humidity.append(i['id'])  # dla wilgotnosci
            elif i['save_graph_data'] == '1' and i['measureUnits'] == '°C':
                fif_graphs_temperature.append(i['id'])  # dla temperatury
        if i['plcid'] in appars: # tylko dla aparow
            if i['save_graph_data'] == '1' and i['measureUnits'] == '%RH':
                apar_graphs_humidity.append(i['id'])  # dla wilgotnosci
            elif i['save_graph_data'] == '1' and i['measureUnits'] == '°C':
                apar_graphs_temperature.append(i['id'])  # dla temperatury

# todo : Problem nie wszystkie maja %RH . Trzeba by bylo w  rej. webhmi zrobic kategorie

print('Ilosc rejestrow z wykresami: {}'.format(len(graphs_all)))
# print(graphs_all)

print('Ilosc rejestrow wilgotnosci z wykresami: {}'.format(len(all_graphs_humidity)))
# print(all_graphs_humidity)

print('Ilosc rejestrow temperatury wykresami: {}'.format(len(all_graphs_temperature)))
# print(all_graphs_temperature)


print('Ilosc rejestrow fif wilgotnosci z wykresami: {}'.format(len(fif_graphs_humidity)))
# print(fif_graphs_humidity)

print('Ilosc rejestrow fif temperatury wykresami: {}'.format(len(fif_graphs_temperature)))
# print(fif_graphs_temperature)

print('Ilosc rejestrow apar wilgotnosci z wykresami: {}'.format(len(apar_graphs_humidity)))
# print(apar_graphs_humidity)

print('Ilosc rejestrow apar temperatury wykresami: {}'.format(len(apar_graphs_temperature)))
# print(apar_graphs_temperature)

# Pobranie wykresow

print('\nDane z wykresow')
wh_start = 1546819261  # start dla wykresu
wh_stop = wh_start + 60 * 60  # 24 h
wh_slices = 4  # minimlana ilosc czesci

for i in fif_graphs_temperature:

    print('Polaczenie dla {}'.format(i))
    time.sleep(2)
    # Ustalenie nagłowka dla wykresu
    headers['X-WH-CONNS'] = ''
    headers['X-WH-REGS'] = str(i)
    headers['X-WH-START'] = str(wh_start)
    headers['X-WH-END'] = str(wh_stop)
    headers['X-WH-SLICES'] = str(wh_slices)
    # displayHeader(headers)
    req3 = getGraphData(device_adress, headers) # odczytanie danych z wykresow
    graphs_data.append(req3)


log = open('graphs.txt', 'w')
print(graphs_data, file=log)
log.close()
