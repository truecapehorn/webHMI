from API_webHMI import *
from defs import *
from head import headers, device_adress

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


graphList=graphListReq()

for i in graphList:
    graphsDict[i['id']] = [i['category'], i['title']]

def graphData(wh_start=1546819261,lenght=60*60*24,wh_slices=4):
    print('\nDane z wykresow')
    wh_stop = wh_start + lenght
    # Ustalenie nagłowka dla wykresu
    headers['X-WH-CONNS'] = ''
    headers['X-WH-REGS'] = ''
    headers['X-WH-START'] = str(wh_start)
    headers['X-WH-END'] = str(wh_stop)
    headers['X-WH-SLICES'] = str(wh_slices)

    graphData=[]
    for k in graphsDict.keys():
        print('Pobranie wykresu {}:{} w {}'.format(k, graphsDict[k][1], graphsDict[k][0]))
        time.sleep(2)
        graphData=graphDataReq(k)  # odczytanie danych z wykresow
        print('-------------\n Wielkosc tablicy', len(graphData))
    return graphData

graphData=graphData()


if __name__=='__main__':
    print(graphsDict)
    print(graphData[0])
    for i in range(4):
        print('.')
    print(graphData[-1])
    print('\n')


