from datetime import datetime
import os
import re
import graphs_data
import csv

#todo: sworzyc wersje na linuxa i windowsa
#todo: to jescze nie to :(

# Podział na pliki
def save_data(unixtime,graphDatas):
    head=[]
    value=[]
    day = datetime.utcfromtimestamp(unixtime).strftime('%Y-%m-%d')

    try:
        os.mkdir('logi/')
    except FileExistsError:
        pass
    try:
        os.mkdir('logi/dane_{}'.format(day))
    except FileExistsError:
        pass

    for k, v in graphDatas.items():
        # logi = open('C:\\Users\\User\\Documents\\PYCHARM\\GIT\\testy\\startup.txt', 'a', encoding='utf8')
        print('Zapis danych dla Mieszknia {}'.format(k))
        try:
            os.remove('logi/dane_{}/graphs_{}.csv'.format(day,k))
        except FileNotFoundError:
            pass
        log = open('logi/dane_{}/graphs_{}.csv'.format(day,k), 'a')
        head=str(list(v[0].keys()))
        head=re.sub('\ |\[|\]|\"|\'|\;', '', head)
        print(head, file=log)
        for i in v:
            value=str(list(i.values()))
            value = re.sub('\ |\[|\]|\"|\'|\;', '', value)
            print(value, file=log)
        log.close()

def csv_writer(day,k,headers,value):
    with open('logi/dane_{}/graphs_{}.csv'.format(day,k), 'a') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(value)

if __name__=='__main__':
    wh_start = 1547078400
    wh_slices = 400
    print('Pobranie wykresow w dniu {} ilość próbek {}'.format(wh_start, wh_slices))

    graphDatas = graphs_data.datas(wh_start, wh_slices)

    for k, v in graphDatas.items():
        print(k, '>', v)

    save_data(1547078400,graphDatas)