def addBinary(a, b):
    remainder = 0
    i = -1
    if len(a) > len(b):
        res_list = [int(a[x]) for x in range(len(a))]
    else:
        res_list = [int(b[x]) for x in range(len(b))]

    while i >= - len(res_list):
        op1 = 0
        op2 = 0
        if i >= - min(len(a), len(b)):
            op1 = int(a[i])
            op2 = int(b[i])
        else:
            op1 = res_list[i]
        res_list[i] = (op1 + op2 + remainder) % 2
        remainder = (op1 + op2 + remainder) // 2
        i -= 1
    if remainder == 1:
        return '1' + ''.join(map(str, res_list))
    else:
        return ''.join(map(str, res_list))

a = '1010'
b = '1011'
print(addBinary(a, b))
