
# p 2 ---------------------------------------------------------

'''
Представлен список чисел.
Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию,
оформить в виде списка.
Для формирования списка использовать генератор.
'''

from random import randint
from time import sleep

rand_li = [randint(-20, 20) for itm in range(20)]
print(rand_li)

# new list
print(sorted(rand_li))

# sequence
for itm in sorted(rand_li):
    print(itm)
    sleep(0.2)
