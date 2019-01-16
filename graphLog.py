from API_webHMI import *
from defs import *
from head import headers, device_adress
from registers import regList
import os
from datetime import datetime
import re

# Pobranie wykresow
graphsDict = {}


def graphListReq():
    print('\n3 :Graph Req\n')
    # displayHeader(headers)  # wystarczy podstawowy naglowek
    req3 = graphList(device_adress, headers)
    return req3


def graphDataReq(k):
    print('\n4 :Graph Data Req\n')
    # displayHeader(headers)  # wystarczy podstawowy naglowek
    req4 = getGraph(device_adress, headers, k)  # odczytanie danych z wykresow
    return req4


graphList = graphListReq()

for i in graphList[0:2]:  # tymczosow tylmko 2 wykresy
    graphsDict[i['id']] = {'apartment': i['category'], 'category': i['title']}

print(graphsDict)


def graphData(wh_start=1547078400, lenght=60 * 60 * 24*7, wh_slices=400):
    print('\nDane z wykresow')
    wh_stop = wh_start + lenght
    # Ustalenie nagłowka dla wykresu
    headers['X-WH-CONNS'] = ''
    headers['X-WH-REGS'] = ''
    headers['X-WH-START'] = str(wh_start)
    headers['X-WH-END'] = str(wh_stop)
    headers['X-WH-SLICES'] = str(wh_slices)

    graphData = {}
    for k in graphsDict.keys():
        print(graphsDict[k]['category'])
        print('Pobranie wykresu {}:{} w {}'.format(k, graphsDict[k]['category'], graphsDict[k]['apartment']))
        time.sleep(2)
        graphData[graphsDict[k]['apartment'], graphsDict[k]['category']] = graphDataReq(
            k)  # odczytanie danych z wykresow
        print('Wielkosc tablicy: {}\n-------------\n'.format(len(graphData)))

    return graphData


print(regList.keys())
graph = {}
graphDatas = graphData()
print('Lista rejestrow')
# for k, v in regList.items():
#     print(k, ':', v)
# Zamiana klucza
for k, v in graphDatas.items():
    print(k)
    for i in v:
        for key in i.keys():

            if key == 'x':
                # print(" keje w graphah", i[key])
                # print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
                i[key] = datetime.utcfromtimestamp(int(i[key])/1000).strftime('%Y-%m-%d--%H:%M:%S')
        for key in regList.keys():
            if key in i.keys():
                i[regList[key]['plcname']] = i[key]  # zamiana klucza na bardziej przyjazna wersje:)
                # del[i[key]] # skasowanie starego wpisu
                i.pop(key)

print('Po konwersji.\n')
# Zmniejsznie ilosci danych wynikowych. Zostawienie tylko wartosci sredniej z próbki.
for k, v in graphDatas.items():
    # print('Dane dla Mieszknia {} - {} '.format(k[0],k[1]))
    for i in v:
        graph = {key: val.split(';')[2] for (key, val) in i.items() if isinstance(val, str) and key != 'x'}
        i.update(graph)
        # print(i)

# Podział na pliki
def save_data():
    head=[]
    value=[]
    try:
        os.mkdir('logi')
    except FileExistsError:
        pass
    for k, v in graphDatas.items():
        # logi = open('C:\\Users\\User\\Documents\\PYCHARM\\GIT\\testy\\startup.txt', 'a', encoding='utf8')
        print('Dane dla Mieszknia {} - {} '.format(k[0], k[1]))
        try:
            os.remove('logi\\graphs_{}_{}.csv'.format(k[0],k[1]))
        except FileNotFoundError:
            pass
        log = open('logi\\graphs_{}_{}.csv'.format(k[0],k[1]), 'a')
        head=str(list(v[0].keys()))
        head=re.sub('\ |\[|\]|\"|\'|\;', '', head)
        print(head, file=log)
        for i in v:
            value=str(list(i.values()))
            value = re.sub('\ |\[|\]|\"|\'|\;', '', value)
            print(value, file=log)
        log.close()

save_data()

if __name__ == '__main__':

    # os.remove('graphs.txt')
    # log = open('graphs.txt', 'a')
    # for k, v in graphDatas.items():
    #     for i in v:
    #         i = str(i)
    #         print(k, i, file=log)
    # log.close()
    pass
