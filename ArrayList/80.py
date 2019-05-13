class Solution_Double_Point:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        front, back, count = 0, 1, 1
        while back < length:
            if nums[back]==nums[front]:
                if count == 1:
                    front += 1
                    nums[front] = nums[back]
                    back += 1
                    count += 1
                else:
                    back += 1
            else:
                front += 1
                nums[front] = nums[back]
                back += 1
                count = 1
        if length == 0:
            return 0
        else:
            return front + 1

class Solution_Common:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        i = 2
        for num in nums[i:]:
            if num > nums[i-2]:
                nums[i]=num
                i+=1
        return i