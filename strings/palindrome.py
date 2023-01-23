def isPalindrome_1(x):
    x_str = str(x)
    x_reversed = x_str[::-1]
    return x_str == x_reversed


def isPalindrome_2(x):
    if x < 0:
        return False
    div = 1
    while (x // div) >= 10:
        div *= 10
    while x > 0:
        fst = x // div
        lst = x % 10
        if fst != lst:
            return False
        x = (x - lst - (fst * div)) // 10
        div //= 100
    return True


x = 123321
print(isPalindrome_1(x))
print(isPalindrome_2(x))
