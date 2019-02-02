from API_webHMI import *
from head import headers, device_adress
from graphsList import graphsDict
from changeRawData import data_change

def head(wh_start=1547078400, wh_slices=4, lenght=60 * 60 * 23):

    # Ustalenie nagłowka dla wykresu
    wh_stop = wh_start + lenght
    headers['X-WH-CONNS'] = ''
    headers['X-WH-REGS'] = ''
    headers['X-WH-START'] = str(wh_start)
    headers['X-WH-END'] = str(wh_stop)
    headers['X-WH-SLICES'] = str(wh_slices)
    return headers

def graphDataReq(headers,k):
    print('\n4 :Graph Data Req\n')
    # displayHeader(headers)  # wystarczy podstawowy naglowek
    req4 = getGraph(device_adress, headers, k)  # odczytanie danych z wykresow
    return req4


def datas(wh_start=1547078400, wh_slices=4, lenght=60 * 60 * 23):
    # Pobranie zapisanych w webhmi wykresow
    print('\nDane z wykresow')
    rawData = {}
    headers = head(wh_start,wh_slices,lenght)
    # stworzenie slownika z danymi wykresow
    for k in graphsDict.keys():
        print('Pobranie wykresu {} : {} w {}'.format(k, graphsDict[k]['category'], graphsDict[k]['apartment']))
        time.sleep(1)
        rawData[k] = graphDataReq(headers,k)  # odczytanie danych z wykresow
        # print(rawData[k])
        print('-------------\n')
    data = data_change(rawData)  # obrobienie zebranych danych
    return rawData,data


if __name__ == "__main__":
    raw_data,data=datas()
    [print(key, '-', val) for key, val in data.items()]


    pass
