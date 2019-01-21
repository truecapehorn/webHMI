from datetime import datetime
import os
import re
import graphs_data
import csv

#todo: sworzyc wersje na linuxa i windowsa
#todo: to jescze nie to :(


def csv_writer(day,k,headers,rows):
    with open('logi/dane_{}/graphs_{}.csv'.format(day,k), 'w') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)



# Podział na pliki
def save_data(unixtime,graphDatas):
    day = datetime.utcfromtimestamp(unixtime).strftime('%Y-%m-%d')
    try:
        os.mkdir('logi/')
    except FileExistsError:
        pass
    try:
        os.mkdir('logi/dane_{}'.format(day))
    except FileExistsError:
        pass

    for key, val in graphDatas.items():
        print('Zapis danych dla Mieszknia {}'.format(k))
        try:
            os.remove('logi/dane_{}/graphs_{}.csv'.format(day,k))
        except FileNotFoundError:
            pass
        headers=[x.strip() for x in val[0].keys()]
        csv_writer(day,key,headers,val)


if __name__=='__main__':
    wh_start = 1547078400
    wh_slices = 4
    print('Pobranie wykresow w dniu {} ilość próbek {}'.format(wh_start, wh_slices))

    graphDatas = graphs_data.datas(wh_start, wh_slices)

    for k, v in graphDatas.items():
        print(k, '>', v)

    save_data(1547078400,graphDatas)