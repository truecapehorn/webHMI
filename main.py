from connections import connection, fifs, appars
from registers import regList
from graphs_stat import graphs_all, all_graphs_humidity, all_graphs_temperature, fif_graphs_humidity, fif_graphs_temperature, \
    apar_graphs_humidity, apar_graphs_temperature
import graphs_list
import graph_range
import graphs_data
import graphs_save

print('Ilość połaczen : {}'.format(len(connection.keys())))
print(connection)
print('Ilosc Aparow: {}'.format(len(appars)))
print(appars)
print('Ilosc Fifow: {}'.format(len(fifs)))
print(fifs)
print('Lista rejestrów : {}'.format(len(regList.keys())))
print(regList)

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

print("Wybierz zakres danych do pobrania")


wh_start,wh_slices=graph_range.range()

print('Pobranie wykresow w dniu {} ilość próbek {}'.format(wh_start,wh_slices))

graphDatas=graphs_data.datas(wh_start,wh_slices)

for k, v in graphDatas.items():
    print(k, '>', v)

print('Czy chcesz zapisac dane')
graphs_save.save_data(wh_start,graphDatas)


