from datetime import datetime
import time,json
# import pytz
import sys

filepath = 'setup.json' # link do pliku z ustawieniami !!
def json_read(path):
    with open(path,'r') as f:
        data=json.load(f)
    return data


def range():
    data=json_read(filepath) # pobranie potrzbnych danych z pliku z ustawieniami
    wh_slices = data["properties"]["samples"]
    lenght = data["properties"]["lenght"]
    wh_start = ''
    print('Pobierz dane dla dnia: rrrr-mm-dd: ', end='>> ')
    while True:
        try:
            wh_start = input()
            wh_start = [int(i) for i in wh_start.split('-')]
            dt = datetime(wh_start[0], wh_start[1], wh_start[2])
            unixtime = time.mktime(dt.timetuple()) #- time.timezone
            date = datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d  %H:%M:%S')
            break
        except:
            if wh_start != 'q':
                print('Zła date!!\nWprowadz jescze raz date rrrr-mm-dd: ', end='>> ')
            else:
                sys.exit(0)

    return int(unixtime), wh_slices, date, lenght


if __name__ == "__main__":
    unixtime, slices, date = range()
    print(unixtime)
    print(date)
