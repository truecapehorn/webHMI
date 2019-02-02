from datetime import datetime
from graphsList import graphsDict
import graphsData
import os
from defs import csv_writer


def save_data(unixtime, graphDatas):
    day = datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d')
    log_dir = 'logi/dane_{}'.format(day)
    log_dir = log_dir.replace('/', os.sep)
    try:
        os.makedirs(log_dir)
    except FileExistsError:
        pass

    for key, val in graphDatas.items():
        file_path = '{}/{}_wykres_{}_{}.csv'.format(log_dir, key, graphsDict[key]['apartment'],
                                                    graphsDict[key]['category'])
        file_path = file_path.replace('/', os.sep)
        print('Zapis danych dla Wykresu {}'.format(key))
        csv_writer(file_path, val)


if __name__ == '__main__':
    wh_start = 1548892800
    wh_slices = 4
    # print('Pobranie wykresow w dniu {} ilość próbek {}'.format(wh_start, wh_slices))

    graphDatas = graphsData.datas(wh_start, wh_slices)[1]

    for k, v in graphDatas.items():
        print(k, ' : ', v)
    for k, v in graphsDict.items():
        print(k, ' > ', v)
    save_data(1547078400, graphDatas)