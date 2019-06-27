from data_structure import TreeNode
from typing import List

class Solution_Recur:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        lst = list()
        if root:
            self._postorderTraversal(root, lst)
            return lst
        else:
            return lst
        
    def _postorderTraversal(self, root: TreeNode, lst: List):
        for c in (root.left, root.right):
            if c:
                self._postorderTraversal(c, lst)
        lst.append(root.val)

class Solution_Stack:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if root:
            lst = [(root, False)]
            while lst:
                node, vis = lst.pop()
                if vis:
                    res.append(node.val)
                else:
                    lst.append((node, not vis))
                    for c in (node.right, node.left):
                        if c:
                            lst.append((c, vis))
            return res
        else:
            return res