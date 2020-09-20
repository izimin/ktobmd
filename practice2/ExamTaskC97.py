# -*- coding: cp1251 -*-
from pt4exam import *

# solved Zimin

def solve():
    task("ExamTaskC97")

    n = int(input())
    res = ""
    for i in range(n):
        for c in input():
            if not res.__contains__(c):
                res += c

    print(res)


start(solve)
