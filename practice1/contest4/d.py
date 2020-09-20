def solve():
    n = int(input())
    ns = ''.zfill(n - 3)
    print("1%s80" % (ns))
    print("3%s60" % (ns))
    print("5%s40" % (ns))
    print("7%s20" % (ns))
    print("9%s00" % (ns))


solve()
