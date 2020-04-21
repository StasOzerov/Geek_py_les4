
# p 6 ---------------------------------------------------------

'''
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

import sys
import itertools
import time


# p 6(a)
script_name, first_param = sys.argv

try:
    first_param = int(first_param)
    for itm in itertools.count(first_param):
        print(itm)
        time.sleep(0.5)
except ValueError:
    print("Некорректный ввод")


# # p 6(b)
# script_name, el_1, el_2, el_3, el_4, el_5 = sys.argv
#
# my_list = [el_1, el_2, el_3, el_4, el_5]
# for itm in itertools.cycle(my_list):
#     print(itm)
#     time.sleep(0.5)