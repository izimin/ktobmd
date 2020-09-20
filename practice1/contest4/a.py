def to4(num):
    num4 = ''
    while num > 0:
        num4 = str(num % 4) + num4
        num //= 4
    return num4


ops = {'0': '+', '1': '-', '2': '*', '3': '/'}


def getRes(s):
    res = 1
    i = 2
    for c in s:
        op = ops.get(c)
        if op == '+':
            res += i
        elif op == '-':
            res -= i
        elif op == '*':
            res *= i
        else:
            res //= i
        i += 1
    return res


def getEx(s):
    return "((((1{0}2){1}3){2}4){3}5){4}6".format(ops.get(s[0]), ops.get(s[1]), ops.get(s[2]), ops.get(s[3]),
                                                  ops.get(s[4]))


def solve():
    n = int(input())
    is_find = False
    for i in range(1024):
        s = to4(i).zfill(5)
        if getRes(s) == n:
            print(getEx(s))
            is_find = True
    if not is_find:
        print("No solutions")


solve()
