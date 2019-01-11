import requests, json
import time

USER = 'admin'
PASS = 'admin'
device_adress = 'http://80.50.4.62:60043'
headers = {'X-WH-APIKEY': 'D606230FEB2CCF4A3520B334BE0E5A29C1311EB0',
           'Accept': 'application/json',
           'Content-Type': 'application/json',
           'X-WH-CONNS': '1,2',
           'X-WH-START': '1526994016',
           'X-WH-END': '1527052904',
           'X-WH-REG-IDS': '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16',
           }

file1='getCurValue.json'
file2='getLocTime.json'
file3='registerList.json'
file4='getRegLog.json'

def jsonRead(file):
    with open(file, encoding="utf8") as data_file:
        data_item = json.load(data_file)
        #print(data_item)
    return data_item

def registerList():
    '''Zczytanie listy rejestrow webHMI'''
    # ADRESS
    api_adress = '/api/registers/'
    url = device_adress + api_adress
    # GET
    # r = requests.get(url, headers=headers)
    r=jsonRead(file3)
    return r

def getCurValue():
    '''Zczytanie wartosci z rejestru'''
    # ADRESS
    api_adress = '/api/register-values'
    url = device_adress + api_adress
    # GET
    # r = requests.get(url, headers=headers)
    r = jsonRead(file1)
    return r

def getLocTime():
    '''Zczytanie daty UNIX time'''
    # ADRESS
    api_adress = '/api/timeinfo'
    url = device_adress + api_adress
    # GET
    # r = requests.get(url, headers=headers)
    r = jsonRead(file2)
    return r

def getRegLog():
    '''Zczytanie wartosci logow'''
    # ADRESS
    api_adress = '/api/register-log'
    url = device_adress + api_adress
    # GET
    # r = requests.get(url, headers=headers)
    r = jsonRead(file4)
    return r


regLog=getRegLog()

for k,v in regLog.items():
    print(k,v)





