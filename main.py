from connections import connection,fifs,appars
from registers import registers


print('Ilość połaczen : {}'.format(len(connection.keys())))
print(connection)
print('Ilosc Aparow: {}'.format(len(appars)))
print(appars)
print('Ilosc Fifow: {}'.format(len(fifs)))
print(fifs)
print('Lista rejestrów : {}'.format(len(registers)))

