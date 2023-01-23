def romanToInt1(s):
    dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res_number = 0
    i = 0
    while i < len(s):
        if i < len(s) - 1 and dict[s[i]] < dict[s[i + 1]]:
            res_number = res_number + dict[s[i + 1]] - dict[s[i]]
            i += 2
        else:
            res_number += dict[s[i]]
            i += 1
    return res_number

def romanToInt2(s):
    dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res_number = 0
    prev = 0
    for i in s:
        curr = dict[i]
        if curr > prev:
            res_number = res_number + curr - 2 * prev
        else:
            res_number = res_number + curr
        # res_number = (res_number + curr - 2 * prev) if curr > prev else (res_number + curr)
        prev = curr
    return res_number

# string = input('Input roman number: ')
string = 'MCMXCIV'
print(romanToInt1(string))
print(romanToInt2(string))