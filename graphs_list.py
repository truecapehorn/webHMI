from API_webHMI import *
from defs import *
from head import headers, device_adress
from registers import regList


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





def graphData(wh_start=1547078400,wh_slices=400, lenght=60 * 60 * 24) :
    # Pobranie zapisanych w webhmi wykresow
    graphList = graphListReq()
    for i in graphList[0:2]:  # tymczosow tylmko 2 wykresy
        graphsDict[i['id']] = {'apartment': i['category'], 'category': i['title']}
    [print(key,'Miejsce: {}, Czujniki: {}'.format(val['apartment'],val['category'])) for key,val in graphsDict.items()]
    print('\nDane z wykresow')
    wh_stop = wh_start + lenght
    # Ustalenie nagłowka dla wykresu
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
        graphData[graphsDict[k]['apartment'], graphsDict[k]['category']] = graphDataReq(
            k)  # odczytanie danych z wykresow
        #todo: takie tworzenie slownika trzeba zmienic. bez sensu.
        # Juz chyba lepiej uaktulanic graphDataReq.
        # np.: {k:{miejsce:'...',kategoria:'...',dane:[{},{}...]}
        print('-------------\n')
    [print(key,val) for key,val in graphData.items()]

    return graphData

if __name__ == '__main__':
    graphDatas = graphData()
    for k, v in graphDatas.items():
        print(k)
        for i in v:
            # print(i.keys())
            for key in i.keys():
                if key not in regList.keys():
                    if key !='x':
                        print(key,end=',')
                        #todo: dodac  wynik do listy poiterowac i usunac z danych



    pass

#todo: wywalic rejetry w nie używancyh połączeniach, które sa w graphDict
