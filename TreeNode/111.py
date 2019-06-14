from data_structure import TreeNode

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not (root.left or root.right):
            return 1
        else:
            res = list()
            for child in (root.left, root.right):
                if child:
                    res.append(self.minDepth(child))
            return 1+min(res)
