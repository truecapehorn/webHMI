def remove_duplicates(l):
    return sorted(list(set(l)))


filepath = 'logi.txt'
lista=[]
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       # print("Line {}: {}".format(cnt, line.strip()))
       if 'Error! Register' in line:
           # print("Line {}: {}".format(cnt, line.strip()))
           l=line.split(" ")
           lista.append(l[9])

       line = fp.readline()
       cnt += 1

print(remove_duplicates(lista))