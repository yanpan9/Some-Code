from typing import List

class Solution_1:
    def countBits(self, num: int) -> List[int]:
        #[2**m, 2**(m+1)] = [0, 2**m-1]+1
        res = [0]
        if num==0:
            return res
        else:
            length, count = 1, 1
            while length<=num:
                for j in range(count):
                    res.append(1+res[j])
                    length += 1
                count = count<<1
        return res[:num+1]

class Solution_2:
    def countBits(self, num: int) -> List[int]:
        # [even] = [even/2]
        # [odd] = [odd-1]+1
        res = [0]
        if num==0:
            return res
        else:
            for num in range(1, num+1):
                if num%2:
                    res.append(res[-1]+1)
                else:
                    res.append(res[num//2])
        return res