from datetime import datetime
import time



def range():
    wh_slices = 400

    print('Pobierz dane dla dnia: rrrr-mm-dd: ',end='>> ')

    wh_start = input()
    wh_start=wh_start.split('-')
    wh_start=[int(i) for i in wh_start]
    dt = datetime(wh_start[0], wh_start[1], wh_start[2], 1, 1)
    unixtime = time.mktime(dt.timetuple())
    return int(unixtime), wh_slices


if __name__=="__main__":

    day,slices=range()
    day = datetime.utcfromtimestamp(day).strftime('%Y-%m-%d ')
    print(day)
