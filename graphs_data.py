from API_webHMI import *
from head import headers, device_adress
from graphs_list import graphsDict
# from registers import regList
# from datetime import datetime


def graphDataReq(k):
    print('\n4 :Graph Data Req\n')
    # displayHeader(headers)  # wystarczy podstawowy naglowek
    req4 = getGraph(device_adress, headers, k)  # odczytanie danych z wykresow
    return req4

def graphData(wh_start=1547078400,wh_slices=400, lenght=60 * 60 * 24) :
    # Pobranie zapisanych w webhmi wykresow

    print('\nDane z wykresow')
    # Ustalenie nagłowka dla wykresu
    wh_stop = wh_start + lenght
    headers['X-WH-CONNS'] = ''
    headers['X-WH-REGS'] = ''
    headers['X-WH-START'] = str(wh_start)
    headers['X-WH-END'] = str(wh_stop)
    headers['X-WH-SLICES'] = str(wh_slices)

    graphData = {}
    # stworzenie slownika z danymi wykresow
    for k in graphsDict.keys():
        print('Pobranie wykresu {}:{} w {}'.format(k, graphsDict[k]['category'], graphsDict[k]['apartment']))
        time.sleep(2)
        graphData[k] = graphDataReq(k)  # odczytanie danych z wykresow
        #todo: takie tworzenie slownika trzeba zmienic. bez sensu.
        # Juz chyba lepiej uaktulanic graphDataReq.
        # np.: {k:{miejsce:'...',kategoria:'...',dane:[{},{}...]}
        print('-------------\n')

    return graphData

graphData_req=graphData()
[print(key,'-',val) for key,val in graphData_req.items()]



# graph = {}
# def datas(wh_start,wh_slices):
#     graphDatas = graphData(wh_start,wh_slices)
#     for k, v in graphDatas.items():
#         # print(k)
#         for i in v:
#             for key in i.keys():
#
#                 if key == 'x':
#                     # print(" keje w graphah", i[key])
#                     # print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
#                     i[key] = datetime.utcfromtimestamp(int(i[key])/1000).strftime('%Y-%m-%d--%H:%M:%S')
#             for key in regList.keys():
#                 if key in i.keys():
#                     i[regList[key]['plcname']] = i[key]  # zamiana klucza na bardziej przyjazna wersje:)
#                     # del[i[key]] # skasowanie starego wpisu
#                     i.pop(key)
#
#     # Zmniejsznie ilosci danych wynikowych. Zostawienie tylko wartosci sredniej z próbki.
#     for k, v in graphDatas.items():
#         # print('Dane dla Mieszknia {} - {} '.format(k[0],k[1]))
#         for i in v:
#             graph = {key: val.split(';')[2] for (key, val) in i.items() if isinstance(val, str) and key != 'x'}
#             i.update(graph)
#             # print(i)
#     return graphDatas

if __name__=="__main__":
    pass


