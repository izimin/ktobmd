def solve():
    k = int(input())
    s = "1"
    n = 2
    while len(s) <= k:
        s += str(n)
        n += 1

    print(s[k - 1])
solve()