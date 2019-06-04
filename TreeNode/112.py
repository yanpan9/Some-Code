from data_structure import TreeNode

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum = sum - root.val
        if sum==0 and not (root.left or root.right):
            return True
        else:
            return (self.hasPathSum(root.left, sum) or
                    self.hasPathSum(root.right, sum))