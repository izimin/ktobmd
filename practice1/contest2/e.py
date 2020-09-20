def solve():
    x,a,b,c = [int(x) for x in input().split()]

    nums = [False] * (c + 1)

    i = 0
    while True:
        if x > c:
            return
        if nums[x]:
            print(i + 1)
            return
        nums[x] = True
        x = (a * x + b) % c
        i += 1

solve()