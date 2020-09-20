def solve():
    s = input().strip()
    while "  " in s:
        s = s.replace("  ", " ")

    for i in range(2, len(s)):
        if s[i - 2] == '.':
            s = s[:i] + s[i].upper() + s[i + 1:]

    print(s)


solve()
