from data_structure import TreeNode
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = list()
        if root:
            queue = deque([root])
            reverse = False
            while queue:
                length = len(queue)
                level = [0 for _ in range(length)]
                for i in range(length):
                    node = queue.popleft()
                    if reverse:
                        level[-i-1] = node.val
                    else:
                        level[i] = node.val
                    for c in (node.left, node.right):
                        if c:
                            queue.append(c)
                res.append(level)
                reverse = not reverse
        return res