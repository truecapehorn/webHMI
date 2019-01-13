from API_webHMI import *
from defs import *
from head import headers,device_adress

# req2=[]

def request():
    print('\n2 :Registers Req\n')
    # displayHeader(headers)  # wystarczy podstawowy naglowek
    req2 = registerList(device_adress, headers)  # odczytanie listy rejestrow
    return req2

registers=request()




if __name__=='__main__':
    print('Lista rejestrów : {}'.format(len(registers)))
    for i in registers:
        if i['id'] == str(4):
            print(registers)  # przykladopwy ciag danych
        if i['id'] == str(2):
            print(registers)
        print(i)

