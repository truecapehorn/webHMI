from API_webHMI import *
from defs import *
from head import headers, device_adress
from registers import regList


'''
Pobranie listy wykresow
'''
graphsDict = {}

def graphListReq():
    print('\n3 :Graph Req\n')
    # displayHeader(headers)  # wystarczy podstawowy naglowek
    req3 = graphList(device_adress, headers)
    return req3


graphList = graphListReq()



for i in graphList[0:2]:  # tymczosow tylmko 2 wykresy
    graphsDict[i['id']] = {'apartment': i['category'], 'category': i['title']}
[print(key, 'Miejsce: {}, Czujniki: {}'.format(val['apartment'], val['category'])) for key, val in graphsDict.items()]



if __name__ == '__main__':
    [print(i) for i in graphList]



    pass


