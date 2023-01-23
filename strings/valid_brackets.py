def isValid(s):
    check_lst = []
    br_dict = {')': '(',
               ']': '[',
               '}': '{'}
    for i in range(len(s)):
        curr = s[i]
        if curr in br_dict:
            try:
                if check_lst.pop() != br_dict[curr]:
                    return False
            except IndexError:
                return False
        else:
            check_lst.append(curr)
    return not check_lst


s = "{"
print(isValid(s))
