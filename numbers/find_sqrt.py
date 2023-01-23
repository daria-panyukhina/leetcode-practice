def sqrt(x):
    if x == 0:
        return 0
    tmp = 1
    dec = 0
    while (tmp * 10) ** 2 < (x // 10):
        tmp *= 10
        dec += 1
    while dec >= 0:
        while tmp ** 2 <= x:
            res = tmp
            tmp += 1 * (10 ** dec)
        tmp = res
        dec -= 1
    return res


print(sqrt(2377764))
