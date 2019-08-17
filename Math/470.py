from random import randint

def rand7():
    return randint(1,7)

class Solution:
    def rand10(self) -> int:
        c = 0
        while c==0 or c>40:
            a = rand7()-1
            b = rand7()
            c = a*7+b
        c, d = c/4, c//4
        return c if c==d else d+1