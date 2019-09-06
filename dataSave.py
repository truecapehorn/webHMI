from graphsList import graphsDict
import graphsData
import os
import shutil
from defs import csv_writer

import pandas as pd


def save_data(day, graphDatas):

    log_dir = 'logi/dane_{}'.format(day)
    log_dir = log_dir.replace('/', os.sep)
    try:
        os.makedirs(log_dir)
    except FileExistsError:
        print('Usuniecie istniejacego folderu: ', log_dir)
        shutil.rmtree(log_dir)  # usuniecie folderu kotory juz istnieje
        os.makedirs(log_dir)
        pass

    for key, val in graphDatas.items():
        file_path = '{}/{}_wykres_{}_{}.csv'.format(log_dir, key, graphsDict[key]['apartment'],
                                                    graphsDict[key]['category'])
        file_path = file_path.replace('/', os.sep)
        print('Zapis danych dla Wykresu {}'.format(key))
        csv_writer(file_path, val)
    graphDatas={}


if __name__ == '__main__':
    wh_start = 1548892800
    wh_slices = 4
    # print('Pobranie wykresow w dniu {} ilość próbek {}'.format(wh_start, wh_slices))

    rawData = graphsData.datas(wh_start, wh_slices)
    print(rawData.keys())
    data = graphsData.changeData(rawData)
    print(data.keys())

    for k, v in data.items():
        print(k, ' : ', v)
    for k, v in graphsDict.items():
        print(k, ' > ', v)
    save_data(1547078400, data)
