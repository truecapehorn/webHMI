from API_webHMI import *
from defs import *
from head import headers, device_adress
from registers import regList
import os

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

for i in graphList[0:3]:  # tymczosow tylmko 2 wykresy
    graphsDict[i['id']] = {'apartment': i['category'], 'category': i['title']}

print(graphsDict)


def graphData(wh_start=1546819261, lenght=60 * 60 * 24, wh_slices=4):
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
        for key in regList.keys():
            if key in i.keys():
                i[regList[key]['plcname']]=i[key] # zamiana klucza na bardziej przyjazna wersje:)
                # del[i[key]] # skasowanie starego wpisu
                i.pop(key)


print('Po konwersji.\n')
# Zmniejsznie ilosci danych wynikowych. Zostawienie tylko wartosci sredniej z próbki.
for k, v in graphDatas.items():
    print(k)
    for i in v:
        graph = {key: val.split(';')[2] for (key, val) in i.items() if isinstance(val, str)}
        i.update(graph)
        print(i)

if __name__ == '__main__':

    os.remove('graphs.txt')
    log = open('graphs.txt', 'a')
    for k, v in graphDatas.items():
        for i in v:
            i=str(i)
            print(k,i, file=log)
    log.close()
    pass
