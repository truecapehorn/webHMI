from datetime import datetime
import time, json
# import pytz
import sys

filepath = 'setup.json'  # link do pliku z ustawieniami !!


def json_read(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data



def make_date(unixtime):
    date = datetime.fromtimestamp(int(unixtime)).strftime('%Y-%m-%d  %H:%M:%S')
    return date

def range():
    data = json_read(filepath)  # pobranie potrzbnych danych z pliku z ustawieniami
    wh_slices = data["properties"]["samples"]
    length = data["properties"]["length"]
    wh_start = ''

    while True:
        try:
            print('Pobierz dane z dnia: rrrr-mm-dd : ', end='>> ')
            wh_start = input()
            wh_start = [int(i) for i in wh_start.split('-')]
            print('Ile dni mają dotyczyc dane : ', end='>> ')
            dni=input()
            if int(dni)>7:
                dni='7'
            dt = datetime(wh_start[0], wh_start[1], wh_start[2])
            unixtime = time.mktime(dt.timetuple())  # - time.timezone

            break
        except:
            if wh_start != 'q':
                print('Zła date!!\nWprowadz jescze raz date rrrr-mm-dd: ', end='>> ')
            else:
                sys.exit(0)

    return int(unixtime), wh_slices, length, dni


if __name__ == "__main__":
    unixtime, slices,length ,dni = range()
    print(unixtime)
    date=make_date(unixtime)
    print(date)
    print('dni:' , dni)