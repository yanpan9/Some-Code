class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length, index = len(nums), 0
        for i in range(length-1, 0, -1):
            if nums[i]>nums[i-1]:
                index, mark = i, i
                while mark < length:
                    if nums[mark]<=nums[i-1]:
                        break
                    else:
                        mark += 1
                nums[i-1], nums[mark-1] = nums[mark-1], nums[i-1]
                break
        for i in range((length-index)//2):
            nums[index+i], nums[-i-1] = nums[-i-1], nums[index+i]i