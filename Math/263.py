class Solution:
    def isUgly(self, num: int) -> bool:
        if num>=1:
            for i in [2,3,5]:
                while not num%i:
                    num = num//i
            return (num==1)
        else:
            return False