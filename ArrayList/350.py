class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list()
        if len(nums1)>len(nums2):
            nums, nums2dic = nums2, nums1
        else:
            nums, nums2dic = nums1, nums2
        count_dict = dict()
        for num in nums2dic:
            if num in count_dict:
                count_dict[num]+=1
            else:
                count_dict[num]=1
        for num in nums:
            if num in count_dict and count_dict[num]>0:
                res.append(num)
                count_dict[num]-=1
        return res