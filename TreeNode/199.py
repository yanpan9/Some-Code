from data_structure import TreeNode
from typing import List

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        lst = list()
        self.num = -1
        if root:
            self.preOrderTraverse(root, lst, 0)
        return lst
        
    def preOrderTraverse(self, root, lst, cur):
        if cur>self.num:
            lst.append(root.val)
            self.num += 1
        if root.right:
            self.preOrderTraverse(root.right, lst, cur+1)
        if root.left:
            self.preOrderTraverse(root.left, lst, cur+1)