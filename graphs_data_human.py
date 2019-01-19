from datetime import datetime
from registers import regList


def data_change(graphData):
    graph = {}
    for k, v in graphData.items():
        for i in v:
            for key in i.keys():
                #Zmiana daty z unixa na normalna date
                if key == 'x':
                    i[key] = datetime.utcfromtimestamp(int(i[key])/1000).strftime('%Y-%m-%d--%H:%M:%S')
            for key in regList.keys():
                # zamiana klucza na bardziej przyjazna wersje:)
                if key in i.keys():
                    i[regList[key]['plcname']] = i[key]
                    i.pop(key)
            # Zmniejsznie ilosci danych wynikowych. Zostawienie tylko wartosci sredniej z próbki.
            graph = {key: val.split(';')[2] for (key, val) in i.items() if isinstance(val, str) and key != 'x'}
            i.update(graph)
    return graphData


if __name__=="__main__":

    pass