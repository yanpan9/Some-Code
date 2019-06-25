from typing import List

class Solution_PseBinary:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        false =[-1,-1]
        if length:
            low, high = 0, length-1
            while low<=high:
                mid = (low+high)//2
                num = nums[mid]
                if num==target:
                    low, high = mid-1, mid+1
                    while low>=0 and nums[low]==target:
                        low -= 1
                    while high<length and nums[high]==target:
                        high +=1
                    return [low+1, high-1]
                elif num>target:
                    high = mid-1
                else:
                    low = mid+1
            return false
        else:
            return false

class Solution_Binary:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        if left==len(nums) or nums[left]!=target:
            return [-1, -1]
        else:
            right = self.binarySearch(nums, target, False)
            return [left, right-1]
        
    def binarySearch(self, nums, target, left):
        low, high = 0, len(nums)
        while low < high:
            mid = (low+high)//2
            num = nums[mid]
            if num>target or (left and num==target):
                high = mid
            else:
                low = mid+1
        return low