from API_webHMI import *
from defs import csv_writer
from head import headers, device_adress
import pandas as pd
from connections import connections

import os

# req2=[]

regList = {}


def reg():
    print('\n2 :Registers Req\n')
    # displayHeader(headers)  # wystarczy podstawowy naglowek
    req2 = registerList(device_adress, headers)  # odczytanie listy rejestrow
    return req2
registers=pd.DataFrame(reg())
registers.head()


regList = pd.merge(registers,connections[['title','plcid']],on='plcid')
regList.index=regList['id']
print(regList['title_y'].head(30))

if __name__ == '__main__':
    pass