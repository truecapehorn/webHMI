import csv, os


def displayHeader(dic):
    print('\nHeader')
    for k, v in dic.items():
        print(k, ':', v)
    print('\n')


def displayList(list):
    print('\nLista')
    for i in list:
        print(i)
    print('\n')


def makeRegIDs(ids):
    regs = ''
    for i in ids:
        regs = regs + i + ','
    regs = regs[:-1]
    return regs


def csv_writer(file_path, dictionary):
    key_set = set()
    dict_list = list()

    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass

    for dic in dictionary:
        key_set.update(dic.keys())
        dict_list.append(dic)
    keys = list(sorted(list(key_set),reverse=True))
    # keys = list(list(key_set))
    print("Zapis do: ",file_path)
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            w = csv.DictWriter(f, keys, delimiter=',', lineterminator='\n')
            w.writeheader()
            w.writerows(dict_list)
    except IOError as e :
        print('Nie mozna zapisac pliku csv',e)
