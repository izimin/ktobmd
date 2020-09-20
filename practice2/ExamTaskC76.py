# -*- coding: cp1251 -*-
from pt4exam import *

# solved Zimin

def solve():
    task("ExamTaskC76")

    dict = {}

    n = int(input())

    for i in range(n):
        cl, surname, initials, subj, est = input().split()
        key = surname + " " + initials
        if subj == 'Информатика':
            dict[key] = (cl, float(est), 1) if key not in dict else (cl, dict[key][1] + float(est), dict[key][2] + 1)

    is_find = False
    for elem in sorted(dict.items(), key=lambda pair: (int(pair[1][0]), pair[0])):
        mid = elem[1][1] / elem[1][2]
        if mid >= 4.0:
            print(elem[1][0], elem[0], "%.2f" % mid)
            is_find = True

    if not is_find:
        print('Требуемые учащиеся не найдены')


start(solve)
