def lengthOfLastWord(s):
    cnt = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            cnt += 1
        elif s[i] == ' ' and cnt == 0:
            continue
        else:
            break
    return cnt
str = 'hello w55orld'
lengthOfLastWord(str)