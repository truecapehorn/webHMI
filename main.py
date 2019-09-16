import dataRange
import graphsData
import dataSave
import graphsList



'''
Obsluga danych z wykresow na webHMI. Dane połaczenia w pliku head.py

# aby zrobic exeka to :
# zaisntalowac pyinstalera2019-
# pip install pyinstaller
# pip install PyWin32 # jak w windows
# Sprawdzic czy skrypt działa
# python your_script.py
# uruchmoc pyinstalera
# pyinstaller --onefile <your_script_name>.py
# lub : pyinstaller --name webHMI_v08 main.py
# exec bedzie w folderze dist

#dla pendelum nalezy skopiowac pliki hook do: C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\PyInstaller\\hooks

'''



print(40 * '-')
print("\nWybierz zakres danych do pobrania")

wh_start, wh_slices,lenght, dni= dataRange.range()
graphs=graphsList.graphsDict

rawData = {}
data = {}
for i in range(int(dni)):
    day = dataRange.make_date(wh_start)
    print('Pobranie wykresow od dnia {} ({}) ilość próbek {}'.format(day, wh_start, wh_slices, lenght))
    rawData = graphsData.datas(graphs,wh_start, wh_slices)
    data = graphsData.changeData(rawData)
    print('Zapisanie danych:')
    dataSave.save_data(day, data)
    wh_start=wh_start+60*60*24
