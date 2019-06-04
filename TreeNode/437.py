from data_structure import TreeNode

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root:
            number = self.findSum(root, sum)
            for child in (root.left, root.right):
                number += self.pathSum(child, sum)
            return number
        else:
            return 0
        
    def findSum(self, root: TreeNode, sum: int) -> int:
        sum -= root.val
        if sum == 0:
            number = 1
        else:
            number = 0
        for child in (root.left, root.right):
            if child:
                number += self.findSum(child, sum)
        return number