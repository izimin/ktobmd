def solve():
    k = [int(s) for s in input()]
    summ = 0
    for i in k:
        for j in k:
            summ += i * j
    print(summ)


solve()
