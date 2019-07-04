from typing import List

class Solution_Hash:
    def majorityElement(self, nums: List[int]) -> int:
        counter = dict()
        length = len(nums)//2
        for num in nums:
            counter[num] = counter.get(num, 0)+1
        for key,count in counter.items():
            if count>length:
                return key

class Solution_Boyer_Moore:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, None
        for num in nums:
            if count==0:
                candidate = num
            count += (1 if candidate==num else -1)
        
        return candidateS