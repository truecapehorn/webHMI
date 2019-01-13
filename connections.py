from API_webHMI import *
from defs import *
from head import headers,device_adress

connection = {}
appars = []
fifs = []

def request():
    print('1: Connection Req\n')
    # displayHeader(headers)
    req1 = connectionList(device_adress, headers)  # pobranie listy polaczen plc.
    return req1

def devices(req1):

    for i in req1:
      # if i['id']==str(159):
      #     print(i)
      # if i['id']==str(237):
      #     print(i)
      if i['disabled'] == '0':  # branie tylko pod uwage włączone polaczenia
        connection[i['id']] = i['title']  # utworzenie slownika dla id i nazyw polaczenia

    for k, v in connection.items():  # rozdzial na fiy i apary
      if v[0:3] == 'APA':
        appars.append(k)  # apary
      elif v[0:3] == 'FIF':
        fifs.append(k)  # fify
    return connection,appars,fifs

req1=request()
conn=devices(req1)



if __name__ == '__main__':


    print('Ilość połaczen : {}'.format(len(req1[0].keys())))
    print(connection.keys())
    print('Ilosc Aparow: {}'.format(len(req1[1])))
    print(appars)
    print('Ilosc Fifow: {}'.format(len(req1[2])))
    print(fifs)


