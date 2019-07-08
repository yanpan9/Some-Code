from data_structure import TreeNode

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root:
            self.pre = TreeNode(-2**32)
            return self.postOrderTraverse(root)
        else:
            return True
        
    def postOrderTraverse(self, root):
        if root.left:
            if not self.postOrderTraverse(root.left):
                return False
        if root.val>self.pre.val:
            self.pre = root
        else:
            return False
        if root.right:
            if not self.postOrderTraverse(root.right):
                return False
        return True