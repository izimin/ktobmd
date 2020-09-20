def solve():
    n = int(input())
    candidates = [0] * 101
    maxe = 0
    maxi = 0
    for num in input().split():
        num_int = int(num)
        candidates[num_int] += 1
        if candidates[num_int] > maxe:
            maxe = candidates[num_int]
            maxi = num_int
    print(maxi)


solve()
