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