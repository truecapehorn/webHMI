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

wh_start=1547078400
wh_slices=400
lenght=60 * 60 * 24


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


if __name__=="__main__":
    [print(key, '-', val) for key, val in graphData.items()]
    pass


