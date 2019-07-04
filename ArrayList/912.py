from typing import List

class Solution:
    def sortArray_Insert(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(1, length):
            for j in range(i):
                if nums[j]>nums[i]:
                    nums.insert(j, nums.pop(i))
                    break
        return nums
        
    def sortArray_Bubble(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(1, length):
            flag = True
            for j in range(1, length):  
                if nums[j]<nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    flag = False
            if flag:
                break
        return nums

