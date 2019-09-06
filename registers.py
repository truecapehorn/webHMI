
import pandas as pd
from connections import connections
from settings import hmi


import os

# req2=[]

# regList = {}


def reg():
    print('\n2 :Registers Req\n')
    # displayHeader(headers)  # wystarczy podstawowy naglowek
    req2 = hmi.make_req('registerList') # odczytanie listy rejestrow
    return req2
registers=pd.DataFrame(reg())
registers.head()


regList = pd.merge(registers,connections[['title','plcid']],on='plcid')
regList.index=regList['id']

if __name__ == '__main__':
    print(regList['title_y'].head(30))

    pass