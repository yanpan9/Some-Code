from data_structure import TreeNode
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return list()
        else:
            result = list()
            queue = deque([root])
            while queue:
                result.insert(0, [node.val for node in queue])
                length = len(queue)
                for _ in range(length):
                    node = queue.popleft()
                    for child in (node.left, node.right):
                        if child:
                            queue.append(child)
            return result