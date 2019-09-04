from settings import hmi

'''
Pobranie listy wykresow
'''
graphsDict = {}


def graphListReq():
    print('\n3 :Graph Req\n')
    req3= hmi.make_req('graphList')
    return req3


graphList = graphListReq()

# todo: wywalic rejetry w nie używancyh połączeniach, które sa w graphDict


for i in graphList:#[22:25]:  # OKRESLIC ILE WYKRESOW DO POBRANIA
    graphsDict[i['id']] = {'apartment': i['category'], 'category': i['title']}
[print(key, 'Miejsce: {}, Czujniki: {}'.format(val['apartment'], val['category'])) for key, val in graphsDict.items()]



if __name__ == '__main__':
    [print(i) for i in graphList]

    pass
