def solve():
    n = int(input())
    i = 1
    sum1 = 0
    sum2 = 0
    for num in input().split(' '):
        num_int = int(num)
        if num_int % 2 == 0:
            sum2 += num_int
        if i % 2 == 0:
            sum1 += num_int
        i += 1

    print("%d %d" % (sum1, sum2))


solve()