def solve():
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    res = [0] * n
    i = 1
    for el in input().split():
        res[(i + k) % n - 1] = int(el)
        i += 1
    for el in res:
        print(el)
solve()