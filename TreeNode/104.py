from data_structure import TreeNode
from collections import deque

class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if root:
            queue = deque([root])
            depth = 0
            while queue:
                depth += 1
                length = len(queue)
                for _ in range(length):
                    node = queue.popleft()
                    for c in (node.left, node.right):
                        if c:
                            queue.append(c)
        return depth