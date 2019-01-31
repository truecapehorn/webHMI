import os


'''
Analiza polaczen z błedem odczytu.
logi ze strony wkliec do pliku logi
zapis listy do errory
'''


def strip_and_remove(l, stripp):
    lista = [int(i.strip(stripp)) for i in list(set(l))]
    return sorted(lista)


def search_file(line, char, cnt=1):
    if 'Error' in line:
        result = line.find(char)
        if result != -1:
            print('L{} - {} i conn find na {}'.format(cnt, line.strip(), result))
            line = line[result:].split(" ")
            line = [i.strip() for i in line]
    return line


def save_con(path, lista):
    errory = open(path, 'a')
    print(lista, file=errory)


def open_file(path):
    lista = []
    with open(path) as fp:
        line = fp.readline()
        cnt = 0
        while line:
            l = search_file(line, 'conn #', cnt)
            if isinstance(l, list):
                lista.append(l[1])
            line = fp.readline()
            cnt += 1
    print('\n', 80 * '-')
    return lista


if __name__ == '__main__':
    filepath_open = 'debuging{}logi.txt'.format(os.sep)
    filepath_save = 'debuging{}errory.txt'.format(os.sep)

    lista = open_file(filepath_open)
    err = strip_and_remove(lista, '#')

    print('Lista połączen z errorem:')
    print(err)
    save_con(filepath_save, err)
