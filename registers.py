from API_webHMI import *
from defs import *
from head import headers, device_adress
from connections import connection

# req2=[]

regList = {}


def request():
    print('\n2 :Registers Req\n')
    # displayHeader(headers)  # wystarczy podstawowy naglowek
    req2 = registerList(device_adress, headers)  # odczytanie listy rejestrow
    return req2


registers = request()

# Stworzenie krótrzego  slownika rejestrow z nazwami połaczen.
for r in registers:
    if r['plcid'] in connection.keys():  # uwzglednia tylko wlaczone polaczenia
        regList[r['id']] = {'plcid': r['plcid'], 'plcname': connection[r['plcid']], 'regtitle': r['title']}

if __name__ == '__main__':

    print('Lista rejestrów : {}'.format(len(regList)))
    # for i in registers:
    #     if i['id'] == str(4):
    #         print(i)  # przykladopwy ciag danych
    #     if i['id'] == str(2):
    #         print(i)
    I1sum = []
    I2sum = []
    I3sum = []
    P1sum = []
    P2sum = []
    P3sum = []
    S1sum = []
    S2sum = []
    S3sum = []
    Q1sum = []
    Q2sum = []
    Q3sum = []
    Ep = []
    Eq = []
    for k, v in regList.items():
        if 'LE03' in v['plcname'] and v['plcname'] != 'LE03_SUM':
            if v['plcname']=='LE03_02.2':
                print(k,v)


            if 'Natezenie pradu L1' in v['regtitle']:
                # print(k, v)
                I1sum.append(k)
                I1sum=[int(i) for i in I1sum]
            if 'Natezenie pradu L2' in v['regtitle']:
                # print(k, v)
                I2sum.append(k)
                I2sum = [int(i) for i in I2sum]
            if 'Natezenie pradu L3' in v['regtitle']:
                I3sum.append(k)
                I3sum = [int(i) for i in I3sum]


            if 'Moc czynna L1' in v['regtitle']:
                # print(k, v)
                P1sum.append(k)
                P1sum = [int(i) for i in P1sum]
            if 'Moc czynna L2' in v['regtitle']:
                # print(k, v)
                P2sum.append(k)
                P2sum = [int(i) for i in P2sum]
            if 'Moc czynna L3' in v['regtitle']:
                P3sum.append(k)
                P3sum = [int(i) for i in P3sum]

            if 'Moc pozorna L1' in v['regtitle']:
                # print(k, v)
                S1sum.append(k)
                S1sum = [int(i) for i in S1sum]
            if 'Moc pozorna L2' in v['regtitle']:
                # print(k, v)
                S2sum.append(k)
                S2sum = [int(i) for i in S2sum]
            if 'Moc pozorna L3' in v['regtitle']:
                S3sum.append(k)
                S3sum = [int(i) for i in S3sum]

            if 'Moc bierna L1' in v['regtitle']:
                # print(k, v)
                Q1sum.append(k)
                Q1sum = [int(i) for i in Q1sum]
            if 'Moc bierna L2' in v['regtitle']:
                # print(k, v)
                Q2sum.append(k)
                Q2sum = [int(i) for i in Q2sum]
            if 'Moc bierna L3' in v['regtitle']:
                Q3sum.append(k)
                Q3sum = [int(i) for i in Q3sum]


    print('--PRAD')
    print('local I1_l =',I1sum)
    print('local I2_l =',I2sum)
    print('local I3_l =',I3sum)

    print('--MOC CZYNNA')
    print('local P1sum_l =',P1sum)
    print('local P2sum_l =',P2sum)
    print('local P3sum_l =',P3sum)

    print('--MOC POZORNA')
    print('local S1sum_l =',S1sum)
    print('local S2sum_l =',S2sum)
    print('local S3sum_l =',S3sum)

    print('--MOC BIERNA')
    print('local Q1sum_l =',Q1sum)
    print('local Q2sum_l =',Q2sum)
    print('local Q3sum_l =',Q3sum)