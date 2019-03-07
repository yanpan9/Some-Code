import numpy as np
def longestPalindrome_DP(s):
    if not s:
            return ""
    if len(s)<2 or s==s[::-1]:
        return s
    length = len(s)+1
    array = [[0 for _ in range(length)] for _ in range(length)]
    for st in range(length):
        array[st][st]=1
    for st in range(length-1):
        array[st][st+1]=1
    for i in range(2, length-1):
        flag = False
        for st in range(length-i):
            for ed in range(st+i, length):
                if s[st]==s[ed-1] and array[st+1][ed-1]==1:
                    array[st][ed]=1
                    flag=True
        if not flag:
            break
    for row in array:
        print(row)
    for i in range(length):
        for j in range(length):
            if array[i][j]==1:
                array[i][j]=j-i
    max_length = max([max(row) for row in array])
    if max_length == 0:
        return None
    else:
        for i in range(length):
            for j in range(length):
                if array[i][j]==max_length:
                    return s[i:j]

if __name__ == "__main__":
    print(longestPalindrome_DP("dsfhhgafusihhasdhjzh"))