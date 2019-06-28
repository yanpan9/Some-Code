from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ht = dict()
        for idx,num in enumerate(nums):
            if num in ht:
                if idx-ht[num]<=k:
                    return True
                else:
                    ht[num]=idx
            else:
                ht[num]=idx
        else:
            return False