from data_structure import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        length = len(nums)
        if length == 0:
            return None
        else:
            idx = length//2
            node = TreeNode(nums[idx])
            node.left = self.sortedArrayToBST(nums[:idx])
            node.right = self.sortedArrayToBST(nums[idx+1:])
            return node