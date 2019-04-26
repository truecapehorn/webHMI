from API_webHMI import *
from head import headers, device_adress
# from graphsList import graphsDict
import pandas as pd
from registers import regList
# %matplotlib inline
import matplotlib.pyplot as plt
from dataRange import make_date


def head(wh_start=1547078400, wh_slices=4, lenght=1):
    # Ustalenie nagłowka dla wykresu
    wh_stop = wh_start + lenght * 60 * 60 * 24
    headers['X-WH-CONNS'] = ''
    headers['X-WH-REGS'] = ''
    headers['X-WH-START'] = str(wh_start)
    headers['X-WH-END'] = str(wh_stop)
    headers['X-WH-SLICES'] = str(wh_slices)
    return headers


def graphDataReq(headers, k):
    print('\n4 :Graph Data Req\n')
    # displayHeader(headers)  # wystarczy podstawowy naglowek
    req4 = getGraph(device_adress, headers, k)  # odczytanie danych z wykresow
    return req4


def datas(graphsDict,wh_start=1547078400, wh_slices=200, lenght=1):
    # Pobranie zapisanych w webhmi wykresow
    date=make_date(wh_start)
    print('\nDane z wykresow dla dnia : ', date )
    rawData = {}
    headers = head(wh_start, wh_slices, lenght)
    # stworzenie slownika z danymi wykresow
    for k in graphsDict.keys():
        print('Pobranie wykresu {} : {} w {} dla dnia {}'.format(k, graphsDict[k]['category'], graphsDict[k]['apartment'], date))
        time.sleep(1)
        raw=graphDataReq(headers, k)
        raw_pd = pd.DataFrame(raw)
        rawData[k]=raw_pd
        print('-------------')
    return rawData


def changeData(rawData):
    data={}
    for k,v in rawData.items():
        wykres=v
        wykres['x'] = pd.to_datetime(wykres['x'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('Europe/Warsaw')

        old_names = wykres.columns.tolist()
        new_names = ['{}_{}'.format(i, regList['title_y'].loc[i]) for i in old_names if i != 'x']
        wykres.rename(columns=dict(zip(old_names, new_names)), inplace=True)
        wykres.head()
        wind = pd.DataFrame(dict([(('Time', ''), wykres['x'])]))
        dd = [wind]
        # dd=[]
        # print(wykres.keys().tolist())
        for i in wykres.keys():
            if i != 'x':
                vals = ['min', 'avg', 'max']
                devs = wykres[i].str.split(';', expand=True).rename(columns=lambda x: vals[x])
                dfp = pd.DataFrame(dict([
                    ((i, 'min'), devs['min'].astype('float')),
                    ((i, 'avg'), devs['avg'].astype('float')),
                    ((i, 'max'), devs['max'].astype('float')),
                ]))
                dd.append(dfp)
        df = pd.concat(dd, axis=1)
        df.set_index('Time', inplace=True)
        # ogranicznie tylko do kolumn z avg
        lista = [x for x in df.columns.tolist() if x[1] == 'avg']
        mask = df[lista]
        data[k]=mask
    return data





if __name__ == "__main__":
    rawData = datas()
    print(rawData.keys())
    data = changeData(rawData)
    tabele_list=list(data.keys())
    wykres=data[tabele_list[1]]






    # wykres.plot(figsize=(15, 5))
    # plt.title("Title")
    # plt.xlabel("Data")
    # plt.ylabel("C")
    # plt.grid(True)
    # plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    # plt.show()



    pass
