class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(nums):
            if len(nums)==1:
                yield nums
            else:
                for idx in range(len(nums)):
                    ele = nums[idx:idx+1]
                    for res in permutation(nums[:idx]+nums[idx+1:]):
                        yield ele+res
        return list(permutation(nums))