from API_webHMI import *
from head import headers, device_adress

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

# todo: wywalic rejetry w nie używancyh połączeniach, które sa w graphDict


for i in graphList:  # [0:2]:  # tymczosow tylko 2 wykresy!!!!!!!!!!!!
    graphsDict[i['id']] = {'apartment': i['category'], 'category': i['title']}
[print(key, 'Miejsce: {}, Czujniki: {}'.format(val['apartment'], val['category'])) for key, val in graphsDict.items()]

if __name__ == '__main__':
    [print(i) for i in graphList]

    pass
