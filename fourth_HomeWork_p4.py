
# p 4 ---------------------------------------------------------

'''
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
'''

from random import randint

rand_li = [randint(-10, 10) for itm in range(20)]
print(rand_li)


# first variant with massive
massiv = [i for i in rand_li if rand_li.count(i) < 2]
print(massiv)


# second variant with sequence
def func_uniq(li):
    for i in li:
        if li.count(i) < 2:
            yield i

for itm in func_uniq(rand_li):
    print(itm)
