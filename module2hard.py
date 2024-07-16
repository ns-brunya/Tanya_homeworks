def proverka(m,n):
    puk = '12', '13', '1423', '121524', '162534', '13172635', '1218273645', '141923283746', '11029384756', '12131511124210394857', '112211310495867', '1611325212343114105968', '1214114232133124115106978', '1317115262143531341251161079', '11621531441351261171089', '12151811724272163631545414513612711810', '118217316415514613712811910', '13141911923282183731746416515614713812911'
    for el in range(len(puk)):
        if m==puk[el]:
            l=el+3
    if l==n:
        return print('you alive')
    else:
        return print('you died')

import random

a = random.randint(3, 20)
spisok = list()
parol=''
print(a)
for i in 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19:
    for j in range(i,20,1):
        d = i + j

        if a % d == 0 and j!=i:
            spisok.append(i)
            spisok.append(j)
for k in spisok:
    parol+=str(k)
print(parol)
proverka(parol,a)
