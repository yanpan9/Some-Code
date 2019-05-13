class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = dict()
        for idx,num in enumerate(nums):
            sub_val = target - num
            if sub_val in res:
                return [res[sub_val], idx]
            res[num]=idx