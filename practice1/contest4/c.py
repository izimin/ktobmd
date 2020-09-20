def solve():
    s = input().strip()
    while "  " in s:
        s = s.replace("  ", " ")

    for el in sorted(s.split()):
        print(el.title())


solve()
