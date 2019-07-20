class Solution_Iter:
	# Just count the number of current permutation
	# Break the time limitation
    def getPermutation(self, n: int, k: int) -> str:
        self.count = k
        self.permutation(list(), list(range(1, n+1)))
        self.lst = [str(i) for i in self.lst]
        return "".join(self.lst)
        
    def permutation(self, lst, nums):
        if not nums:
            self.count -= 1
            if self.count == 0:
                self.lst = lst[:]
                return False
            else:
                return True
        else:
            for idx,num in enumerate(nums):
                lst.append(num)
                if not self.permutation(lst, nums[:idx]+nums[idx+1:]):
                    return False
                lst.pop()
            return True

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        lst = [1,]
        for i in range(1, n):
            lst.append(lst[-1]*i)
        indices = list()
        k = k-1
        for i in range(n):
            r, k = divmod(k, lst.pop())
            indices.append(r)
        nums = list(range(1,n+1))
        res = [str(nums.pop(idx)) for idx in indices]
        return "".join(res)