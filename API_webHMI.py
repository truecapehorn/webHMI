import requests, json
import time


def response_status(action, r):
    '''Wydrukowanie wynikow'''
    # Response, status etc
    print('\n' + 140 * '-' + '\n')
    print('* {0} dla URL: {1}\n  Kodowanie znaków: {2}\n'.format(action, r.url,r.apparent_encoding))
    print('* ODPOWIEDZ SERWERA:\n{0}'.format(r.text))  # TEXT/HTML
    print('* KOD STATUSU I STATUS:\n[{0} --> {1}]\n'.format(r.status_code, r.reason))  # HTTP
    print('* NAGLOWEK ODPOWIEDZI:\n{0}\n'.format(r.headers))
    print('<!---------koniec-----------!>')


def connectionList(device_adress,headers):
    '''Zczytanie listy połaczen webHMI'''
    # ADRESS
    api_adress = '/api/connections'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)

    return r.json()


def registerList(device_adress,headers):
    '''Zczytanie listy rejestrow webHMI'''
    # ADRESS
    api_adress = '/api/registers/'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    return r.json()


def trendList(device_adress,headers):
    '''Zczytanie listy trendow webHMI'''
    # ADRESS
    api_adress = '/api/trends/'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    return r.json()


def graphList(device_adress,headers):
    '''Zczytanie listy grafow webHMI'''
    # ADRESS
    api_adress = '/api/graphs/'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    return r.json()


def getCurValue(device_adress,headers):
    '''Zczytanie wartosci z rejestru'''
    # ADRESS
    api_adress = '/api/register-values'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    return r.json()

def getLocTime(device_adress,headers):
    '''Zczytanie daty UNIX time'''
    # ADRESS
    api_adress = '/api/timeinfo'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    return r.json()

def getRegLog(device_adress,headers):
    '''Zczytanie wartosci logow'''
    # ADRESS
    api_adress = '/api/register-log'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    return r.json()

def getGraphData(device_adress,headers):
    '''Zczytanie wartosc i wykresow'''
    # ADRESS
    api_adress = '/api/graph-data/'
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    action='pobranie wykresow'
    response_status(action,r)
    return r.json()

def getGraph(device_adress,headers,graphID):
    '''Zczytanie wartosc i wykresow ale dla konkretnego'''
    # ADRESS
    api_adress = '/api/graph-data/{}'.format(graphID)
    url = device_adress + api_adress
    # GET
    r = requests.get(url, headers=headers)
    action='pobranie wykresow'
    response_status(action,r)
    return r.json()








if __name__ == "__main__":

    # USER = 'admin'
    # PASS = 'elam4321'
    device_adress = 'http://80.50.4.62:60043'

    headers = {'X-WH-APIKEY': 'D606230FEB2CCF4A3520B334BE0E5A29C1311EB0',
               'Accept': 'application/json',
               'Content-Type': 'application/json',
               'X-WH-CONNS': '1,2,3,4,5',
               'X-WH-START': '1546819261',
               'X-WH-END': '1547123883',
               'X-WH-REG-IDS': '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16',
               'X-WH-SLICES': '400',
               'X-WH-REGS': '1,2,3,4',
               }

    a = 1

    l = []

    dict1 = registerList(device_adress,headers)
    print(len(dict1))
    for i in dict1:
        print(i)
        pass

    while True:
        dict2 = getCurValue(device_adress,headers)
        print('pomiar ', a)
        #print(getLocTime()['timestamp'])
        timestamp=getLocTime(device_adress,headers)['timestamp']

        for i in range(len(dict1)):
            ids = dict1[i]['id']
            print(dict1[i]['title'], dict2[str(ids)]['v'])
            l.append(dict2[str(ids)]['v'])

        log = open('log.txt', 'a')
        print(timestamp,',',l, file=log)
        log.close()
        l=[]

        time.sleep(0)
        a += 1
        break
    #print(getRegLog())

    dict3=getRegLog(device_adress,headers)
    print(dict3)
    for i in dict3:
        if i['r']==2:
            logi = open('logi.txt', 'a')
            print(i['r'], ',', i['t'], ',', i['v'], file=logi)
            logi.close()

    dict4=graphList(device_adress,headers)
    for i in dict4:
        print(i)

    dict5=getGraphData(device_adress,headers)
    print(len(dict5))
    for i in dict5:
        print(i)
    print('\nconnection')
    dict6=connectionList(device_adress,headers)
    for i in dict6:
        print(i)
    for i in dict6:
        print(i['id'])



