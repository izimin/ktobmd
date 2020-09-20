# -*- coding: cp1251 -*-
from pt4exam import *

# solved Zimin

def solve():
    task("ExamTaskC34")

    dict_counts = {}

    n = int(input())
    for i in range(n):
        name, school, year = input().split()
        dict_counts[school] = 1 if school not in dict_counts else dict_counts[school] + 1

    for elem in sorted(dict_counts.items(), key=lambda pair: (pair[1], int(pair[0]))):
        print(elem[1], elem[0])


start(solve)
