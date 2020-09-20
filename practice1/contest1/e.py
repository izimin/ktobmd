def solve():
    s = input().split(' ')
    n = int(s[0])
    n2 = n * 2
    k = int(s[1])

    count = 0
    while n < n2:
        n += n * k / 100
        count += 1

    print(count)

solve()
