from data_structure import Node
from collections import deque
from typing import List

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = list()
        if root:
            queue = deque([root])
            while queue:
                sub_res = list()
                for _ in range(len(queue)):
                    node = queue.popleft()
                    sub_res.append(node.val)
                    queue.extend(node.children)
                res.append(sub_res)
        return res