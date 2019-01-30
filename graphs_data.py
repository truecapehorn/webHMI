from API_webHMI import *
from head import headers, device_adress
from graphs_list import graphsDict
from graphs_data_human import data_change


def graphDataReq(k):
    print('\n4 :Graph Data Req\n')
    # displayHeader(headers)  # wystarczy podstawowy naglowek
    req4 = getGraph(device_adress, headers, k)  # odczytanie danych z wykresow
    return req4


def datas(wh_start=1547078400, wh_slices=4, lenght=60 * 60 * 23):
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
        time.sleep(0.5)
        graphData[k] = graphDataReq(k)  # odczytanie danych z wykresow
        print('-------------\n')
    graphData = data_change(graphData)
    return graphData


if __name__ == "__main__":
    [print(key, '-', val) for key, val in datas().items()]

    pass
