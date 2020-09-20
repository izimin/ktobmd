def solve():
    k = int(input())
    s = '1'
    num = 1
    while len(s) < k + 1:
        num *= 10
        s += str(num)

    print(s[k-1])

solve()
