from connections import connection, fifs, appars
from registers import regList
from reg_stat import graphs_all, all_graphs_humidity, all_graphs_temperature, fif_graphs_humidity, fif_graphs_temperature, \
    apar_graphs_humidity, apar_graphs_temperature
import graph_range
import graphs_data
import graphs_save

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

print('Ilość połaczen : {}'.format(len(connection.keys())))
# print(connection)
print('Ilosc Aparow: {}'.format(len(appars)))
# print(appars)
print('Ilosc Fifow: {}'.format(len(fifs)))
# print(fifs)
print('Lista rejestrów : {}'.format(len(regList.keys())))
# print(regList)

print('Ilosc rejestrow z wykresami: {}'.format(len(graphs_all)))
# print(graphs_all)

print('Ilosc rejestrow wilgotnosci z wykresami: {}'.format(len(all_graphs_humidity)))
# print(all_graphs_humidity)

print('Ilosc rejestrow temperatury wykresami: {}'.format(len(all_graphs_temperature)))
# print(all_graphs_temperature)

print('Ilosc rejestrow fif wilgotnosci z wykresami: {}'.format(len(fif_graphs_humidity)))
# print(fif_graphs_humidity)

print('Ilosc rejestrow fif temperatury wykresami: {}'.format(len(fif_graphs_temperature)))
# print(fif_graphs_temperature)

print('Ilosc rejestrow apar wilgotnosci z wykresami: {}'.format(len(apar_graphs_humidity)))
# print(apar_graphs_humidity)

print('Ilosc rejestrow apar temperatury wykresami: {}'.format(len(apar_graphs_temperature)))
# print(apar_graphs_temperature)

print(40*'-')
print("\nWybierz zakres danych do pobrania")


wh_start,wh_slices,date=graph_range.range()

print('Pobranie wykresow w dniu {} ({}) ilość próbek {}'.format(date,wh_start,wh_slices))

graphDatas=graphs_data.datas(wh_start,wh_slices)

# for k, v in graphDatas.items():
#     print(k, '>', v)

print('Zapisanie danych:')
graphs_save.save_data(wh_start,graphDatas)

#todo: Zastosowac plik konfiguracyjny do pobieraania wlasciwosci polaczenia lub pytac uzytkownika jaki adres chcesz pytac.

