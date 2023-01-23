def longestCommonPrefix(strs):
    res = strs[0]
    for i in range(1, len(strs)):
        next_word = strs[i]
        size = min(len(res), len(next_word))
        tmp_str = ''
        for j in range(size):
            if res[j] != next_word[j]:
                break
            else:
                tmp_str+= res[j]
        res = tmp_str
    return res


# my_lst = [str(x) for x in input().split()]
my_lst = ["baab","bacb","b","cbc"]
l1 = ["flower","flow","flight"]
l2 = ["cir","car"]
print(longestCommonPrefix(my_lst))
print(longestCommonPrefix(l1))
print(longestCommonPrefix(l2))
