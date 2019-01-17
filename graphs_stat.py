
from registers import registers
from connections import connection, appars, fifs

graphs_all = []
all_graphs_humidity = []
all_graphs_temperature = []
fif_graphs_humidity = []
fif_graphs_temperature = []
apar_graphs_humidity = []
apar_graphs_temperature = []

# Ustalenie jakie rejstry mają wykresy
for i in registers:
    if i['plcid'] in connection.keys():  # uwzglednia tylko wlaczone polaczenia
        if i['save_graph_data'] == '1':
            graphs_all.append(i['id'])  # dla wszystkich ktore maja wykresy
            if i['measureUnits'] == '%RH':
                all_graphs_humidity.append(i['id'])  # dla wilgotnosci
            elif i['measureUnits'] == '°C' and i['title'] != 'Punkt rosy/szronu':
                all_graphs_temperature.append(i['id'])  # dla temperatury

            if i['plcid'] in fifs:  # tylko dla fifow
                if i['measureUnits'] == '%RH':
                    fif_graphs_humidity.append(i['id'])  # dla wilgotnosci
                elif i['measureUnits'] == '°C':
                    fif_graphs_temperature.append(i['id'])  # dla temperatury
            if i['plcid'] in appars:  # tylko dla aparow
                if i['measureUnits'] == '%RH':
                    apar_graphs_humidity.append(i['id'])  # dla wilgotnosci
                elif i['measureUnits'] == '°C' and i['title'] != 'Punkt rosy/szronu':
                    apar_graphs_temperature.append(i['id'])  # dla temperatury

# todo : Problem nie wszystkie maja %RH . Trzeba by bylo w  rej. webhmi zrobic kategorie

if __name__ == '__main__':
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
