from data_structure import TreeNode
from typing import List

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = list()
        def dfs(lst, sum_):
            node = lst[-1]
            if node.left:
                lst.append(node.left)
                sum_ += node.left.val
                dfs(lst, sum_)
                lst.pop()
                sum_ -= node.left.val
            if node.right:
                lst.append(node.right)
                sum_ += node.right.val
                dfs(lst, sum_)
                lst.pop()
                sum_ -= node.right.val
            if sum_==sum and not(node.left or node.right):
                res.append([ele.val for ele in lst])
        if root:
            dfs([root,], root.val)
        return res