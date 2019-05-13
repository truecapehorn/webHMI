import datetime
import time, json
import pytz
import sys

filepath = 'setup.json'  # link do pliku z ustawieniami !!

local_tz = pytz.timezone ('Europe/Warsaw')


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
            if int(dni)>31:
                dni='31'
            datetime_without_tz = datetime.datetime.strptime(f"{wh_start[0]}-{wh_start[1]}-{wh_start[2] - 1} 23:00:00","%Y-%m-%d %H:%M:%S")
            datetime_with_tz = local_tz.localize(datetime_without_tz, is_dst=True)
            datetime_in_utc = datetime_with_tz.astimezone(pytz.utc)

            datetime_without_tz_ts = time.mktime(datetime_without_tz.timetuple())
            datetime_with_tz_ts = time.mktime(datetime_with_tz.timetuple())
            datetime_in_utc_ts = time.mktime(datetime_in_utc.timetuple())

            str1 = datetime_without_tz.strftime('%Y-%m-%d %H:%M:%S %Z')
            str2 = datetime_with_tz.strftime('%Y-%m-%d %H:%M:%S %Z')
            str3 = datetime_in_utc.strftime('%Y-%m-%d %H:%M:%S %Z')


            unixtime = datetime_in_utc_ts # uzycie czasu UTC dla webHMI

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