# -*- coding: cp1251 -*-
from pt4exam import *

# solved Zimin

def solve():
    task("ExamTaskC123")

    num_prev = int(input())
    first = num_prev
    count = 0

    while True:
        num_cur = int(input())

        if num_cur <= num_prev:
            h = num_prev - first
            if h > first:
                print(h)
                count += 1
            first = num_cur

        if num_cur == 0:
            break

        num_prev = num_cur

    print(count)


start(solve)
