
import pandas as pd
from API_webHMI import *
from head import headers, device_adress
from settings import hmi


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# connection = {}
# appars = []
# fifs = []


def conn():
    print('1: Connection Req\n')
    # displayHeader(headers)
    req1 = hmi.make_req('connectionList') # pobranie listy polaczen plc.
    return req1


def devices():
    req1 = conn()
    connections = pd.DataFrame(req1)
    connections['plcid'] = connections['id']
    connections.index = connections['id']
    # connections.head()
    return connections


connections=devices()

if __name__ == '__main__':
    dv=devices()
    print(dv.head())
    pass
