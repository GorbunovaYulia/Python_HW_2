#"""
#Ќа столе лежат n монеток. Ќекоторые из них лежат вверх решкой, а некоторые Ц гербом. 
#ќпределите минимальное число монеток, которые нужно перевернуть, 
#чтобы все монетки были повернуты вверх одной и той же стороной. 
#¬ыведите минимальное количество монет, которые нужно перевернуть
#"""

from random import randint
n = randint(1,10)
counterzero=0
counterfirst=0
for i in range(1,n+1):
    i = randint(0,1)
    print(i)
    if i==0:
        counterzero+=1
    else:
        counterfirst+=1
if counterzero<counterfirst:
    print(f"Ќаименьшее количество монет, которые нужно перевернуть =  {counterzero}")
else:
    print(f"Ќаименьшее количество монет, которые нужно перевернуть =  {counterfirst}")














