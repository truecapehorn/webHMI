
import dataRange
import graphsData
import dataSave

'''
Obsluga danych z wykresow na webHMI. Dane połaczenia w pliku head.py

# aby zrobic exeka to :
# zaisntalowac pyinstalera
# pip install pyinstaller
# pip install PyWin32 # jak w windows
# Sprawdzic czy skrypt działa
# python your_script.py
# uruchmoc pyinstalera
# pyinstaller --onefile <your_script_name>.py
# exec bedzie w folderze dist

'''



print(40 * '-')
print("\nWybierz zakres danych do pobrania")

wh_start, wh_slices, date, lenght = dataRange.range()

print('Pobranie wykresow w dniu {} ({}) ilość próbek {} ilosc dni {}'.format(date, wh_start, wh_slices, lenght))

rawData = graphsData.datas(wh_start, wh_slices)
data = graphsData.changeData(rawData)


print('Zapisanie danych:')

dataSave.save_data(wh_start, data)
