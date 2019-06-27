from data_structure import TreeNode
from typing import List

class Solution_Recur:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        lst = list()
        if root:
            self._preorderTraversal(root, lst)
            return lst
        else:
            return lst
            
    def _preorderTraversal(self, root: TreeNode, lst: List):
        lst.append(root.val)
        for c in (root.left, root.right):
            if c:
                self._preorderTraversal(c, lst)

class Solution_Stack:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if root:
            lst = [root,]
            while lst:
                node = lst.pop()
                res.append(node.val)
                for c in (node.right, node.left):
                    if c:
                        lst.append(c)
            return res
        else:
            return res