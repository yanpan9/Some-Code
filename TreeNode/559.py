from data_structure import Node
from collections import deque

class Solution_Recur:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        elif root.children:
            return 1+max([self.maxDepth(node) for node in root.children])
        else:
            return 1

class Solution_Iter:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        if root:
            queue = deque([root])
            while queue:
                length = len(queue)
                for _ in range(length):
                    node = queue.popleft()
                    for c in node.children:
                        queue.append(c)
                depth += 1
        return depth

