def solve():
    mini = 0
    maxi = 0
    for num in input().split(' '):
        num_int = int(num)
        if num_int != 0:
            if mini == 0 or num_int < mini:
                mini = num_int
            if maxi == 0 or num_int > maxi:
                maxi = num_int

    print("%d %d" % (mini, maxi))
solve()
