
# p 1 ---------------------------------------------------------

'''
Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
'''

from sys import argv

script_name, first_p, second_p, third_p = argv

def salary_calc(workperh, hourlyrate, bonus):
    try:
        workperh = float(workperh)
        hourlyrate = float(hourlyrate)
        bonus = float(bonus)
        if workperh and hourlyrate and bonus >= 0:
            return workperh * hourlyrate + bonus
        else:
            print("Не должно быть отрицательных значений!")
    except ValueError:
        print("Некорректный ввод!")

salary = salary_calc(first_p, second_p, third_p)
rub = int(salary)
cop = round((salary % 1) * 100)
print('Заработная плата сотрудника:', rub, "руб.", cop, "коп.")
