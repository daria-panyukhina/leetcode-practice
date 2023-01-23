def isPalindrome(s):
    res = [x.lower() for x in s if x.isalpha() or x.isdigit()]
    print(res)
    half = len(res) // 2
    i = 0
    j = -1
    while i < half:
        if res[i] != res[j]:
            return False
        i += 1
        j -= 1
    return True

s = "A man, a plan, a canal: Panama"
s1 = "race a car"
s2 = "0P"
# print(isPalindrome(s))
# print(isPalindrome(s1))
print(isPalindrome(s2))
