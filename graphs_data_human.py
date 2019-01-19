from graphs_data import graphData


graph = {}
def datas(wh_start,wh_slices):
    graphDatas = graphData(wh_start,wh_slices)
    for k, v in graphDatas.items():
        # print(k)
        for i in v:
            for key in i.keys():

                if key == 'x':
                    # print(" keje w graphah", i[key])
                    # print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
                    i[key] = datetime.utcfromtimestamp(int(i[key])/1000).strftime('%Y-%m-%d--%H:%M:%S')
            for key in regList.keys():
                if key in i.keys():
                    i[regList[key]['plcname']] = i[key]  # zamiana klucza na bardziej przyjazna wersje:)
                    # del[i[key]] # skasowanie starego wpisu
                    i.pop(key)

    # Zmniejsznie ilosci danych wynikowych. Zostawienie tylko wartosci sredniej z próbki.
    for k, v in graphDatas.items():
        # print('Dane dla Mieszknia {} - {} '.format(k[0],k[1]))
        for i in v:
            graph = {key: val.split(';')[2] for (key, val) in i.items() if isinstance(val, str) and key != 'x'}
            i.update(graph)
            # print(i)
    return graphDatas