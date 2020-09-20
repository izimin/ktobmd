def solve():
    s1, s2 = input().split()
    inter = len(set(s1).intersection(set(s2)))
    b = 0
    for i in range(4):
        if s1[i] == s2[i]:
            b += 1
    print(b)
    print(inter - b)

solve()