'''
Analiza polaczen z błedem odczytu.
logi ze strony wkliec do pliku logi
zapis listy do errory
'''


def remove_duplicates(l):
    lista=[int(i.strip('#')) for i in list(set(l))]
    return sorted(lista)


filepath = 'logi.txt'
lista=[]
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       if 'Error!' in line:

           result = line.find('conn')
           print('L{} - {} i conn find na {}'.format(cnt, line.strip(),result))
           l=line[result:].split(" ")
           lista.append(l[1])
       line = fp.readline()
       cnt += 1
print(30*'-','\n')
err=remove_duplicates(lista)
print('Lista połączen z errorem:')
print(err)
errory=open('errory.txt','a')
print(err, file=errory)