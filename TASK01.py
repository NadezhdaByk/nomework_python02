# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

from random import random

import random

N = int(input('Введите кол-во монеток'))
coins=[]
a=0
b=0
for i in range(N):
    coins.append(random.randint(0,1))
    if coins[i]==0:
        a+=1
    else: b+=1
print(coins)
if a>b:
    print(b)
else: print(a)


