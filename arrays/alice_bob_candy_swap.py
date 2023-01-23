def fairCandySwap(aliceSizes, bobSizes):
    sum_a = 0
    sum_b = 0
    for i in range(max(len(aliceSizes), len(bobSizes))):
        if i >= len(aliceSizes):
            sum_b += bobSizes[i]
        elif i >= len(bobSizes):
            sum_a += aliceSizes[i]
        else:
            sum_a += aliceSizes[i]
            sum_b += bobSizes[i]
    dif = int((sum_a + sum_b) / 2) - min(sum_a, sum_b)
    if len(aliceSizes) > len(bobSizes):
        min_arr = bobSizes
        max_arr = aliceSizes
        if sum_a < sum_b:
            dif = - dif
    else:
        min_arr = aliceSizes
        max_arr = bobSizes
        if sum_a > sum_b:
            dif = - dif
    i = 0
    my_dict = dict()
    for i in range(len(min_arr)):
        my_dict[min_arr[i] + dif] = min_arr[i]
    for i in range(len(max_arr)):
        if max_arr[i] in my_dict:
            res = [max_arr[i], my_dict[max_arr[i]]]
    if max_arr == aliceSizes:
        return res
    else:
        tmp = res[0]
        res[0] = res[1]
        res[1] = tmp
        return res


def fairCandySwap2(aliceSizes, bobSizes):
    sum_a = 0
    sum_b = 0
    for i in range(max(len(aliceSizes), len(bobSizes))):
        if i >= len(aliceSizes):
            sum_b += bobSizes[i]
        elif i >= len(bobSizes):
            sum_a += aliceSizes[i]
        else:
            sum_a += aliceSizes[i]
            sum_b += bobSizes[i]
    dif = int((sum_a + sum_b) / 2) - min(sum_a, sum_b)
    my_dict = dict()
    if sum_a < sum_b:
        for i in range(len(aliceSizes)):
            my_dict[aliceSizes[i] + dif] = aliceSizes[i]
    if sum_a > sum_b:
        for i in range(len(aliceSizes)):
            my_dict[aliceSizes[i] - dif] = aliceSizes[i]

    for i in range(len(bobSizes)):
        if bobSizes[i] in my_dict:
            return [my_dict[bobSizes[i]], bobSizes[i]]




# alice = [1, 1]
# bob = [1, 2, 1, 4]
# # bob = [1, 1]
# # alice = [1, 2, 1, 4]
# alice = [1, 1, 1, 1, 1]
# bob = [7, 4]
# bob = [1, 1, 1, 1, 1]
# alice = [7, 4]

alice = [69,31,57,7,16]
bob =[4,85,14,38,33]

print(fairCandySwap(alice, bob))
print(fairCandySwap2(alice, bob))
