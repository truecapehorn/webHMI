from datetime import datetime
import time
#import pytz



def range():
    wh_slices = 400

    print('Pobierz dane dla dnia: rrrr-mm-dd: ',end='>> ')
    wh_start = input()
    wh_start=[int(i) for i in wh_start.split('-')]
    dt = datetime(wh_start[0], wh_start[1], wh_start[2], 0, 0)
    unixtime = time.mktime(dt.timetuple())
    date=datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d')

    return int(unixtime), wh_slices,date


if __name__=="__main__":

    unixtime,slices,date=range()
    print(unixtime)
    print(date)
