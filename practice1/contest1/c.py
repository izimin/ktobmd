import math


def solve():
    n = int(input())

    for a in range(1, int(math.sqrt(n)) + 1):
        b = math.sqrt(n - a * a)
        if b - float(int(b)) == 0:
            print("YES\n%d %d" % (a, b))
            return

    print("NO")


solve()
