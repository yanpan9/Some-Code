class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        low, high = 0, length-1
        while low < high:
            mid = (low+high)//2
            if nums[mid]>nums[-1]:
                low = mid+1
            else:
                high = mid
        if low == 0:
            low, high = 0, length-1
        elif nums[0]<= target:
            low, high = 0, low-1
        else:
            low, high = low, length-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low = mid+1
            else:
                high = high-1
        else:
            return -1