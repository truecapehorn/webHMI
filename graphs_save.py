from datetime import datetime
from graphs_list import graphsDict
import graphs_data
import csv, os
from defs import csv_writer


# def csv_writer(path, headers, rows):
#     try:
#         with open(path, 'w') as f:
#             f_csv = csv.DictWriter(f, headers, lineterminator='\n')
#             f_csv.writeheader()
#             f_csv.writerows(rows)
#     except IOError:
#         print('Nie mozna zapisac pliku csv')

# Podział na pliki


def save_data(unixtime, graphDatas):
    day = datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d')
    log_dir = 'logi/dane_{}'.format(day)
    log_dir.replace('/', os.sep)

    try:
        os.makedirs(log_dir)
    except FileExistsError:
        pass

    for key, val in graphDatas.items():
        file_path = '{}/{}_wykres_{}_{}.csv'.format(log_dir, key, graphsDict[key]['apartment'],
                                                    graphsDict[key]['category'])
        file_path.replace('/', os.sep)
        print('Zapis danych dla Wykresu {}'.format(key))
        csv_writer(file_path, val)
        #todo: cos trzeba zmienic z danymi od licznikow, bo wszedzie jest albo appators albo bmeters
        #todo: nie zapisuje wykresu 24. nie wiem dlaczego

if __name__ == '__main__':
    wh_start = 1547078400
    wh_slices = 4
    # print('Pobranie wykresow w dniu {} ilość próbek {}'.format(wh_start, wh_slices))

    graphDatas = graphs_data.datas(wh_start, wh_slices)

    for k, v in graphDatas.items():
        print(k, '>', v)

    for k, v in graphsDict.items():
        print(k, '>', v)
    save_data(1547078400, graphDatas)
