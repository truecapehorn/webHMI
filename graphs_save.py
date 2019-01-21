from datetime import datetime
import os
import sys
import re
import graphs_data
import csv

sep=os.sep
#todo: sworzyc wersje na linuxa i windowsa
#todo: to jescze nie to :(


def csv_writer(path,headers,rows):
    try:
        with open(path, 'w') as f:
            f_csv = csv.DictWriter(f, headers,lineterminator='\n')
            f_csv.writeheader()
            f_csv.writerows(rows)
    except IOError:
        print('Nie mozna zapisac pliku csv')

        # Podział na pliki
def save_data(unixtime,graphDatas):
    day = datetime.utcfromtimestamp(unixtime).strftime('%Y-%m-%d')
    log_dir='logi{0}dane_{1}'.format(sep,day)

    try:
        os.makedirs(log_dir)
    except FileExistsError:
        pass

    for key, val in graphDatas.items():
        file_path='{}{}wykres_{}.csv'.format(log_dir,sep,key)
        print('Zapis danych dla Mieszknia {}'.format(key))
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass
        headers=[x.strip() for x in val[0].keys()]
        csv_writer(file_path,headers,val)


if __name__=='__main__':
    wh_start = 1547078400
    wh_slices = 4
    # print('Pobranie wykresow w dniu {} ilość próbek {}'.format(wh_start, wh_slices))

    graphDatas = graphs_data.datas(wh_start, wh_slices)

    for k, v in graphDatas.items():
        print(k, '>', v)

    save_data(1547078400,graphDatas)