from collections import deque

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root:
            queue = deque([(root, None)])
            while queue:
                length = len(queue)
                level = dict()
                for _ in range(length):
                    node, parent = queue.popleft()
                    level[node.val]=parent
                    for c in (node.left,node.right):
                        if c:
                            queue.append((c, node.val))
                if x in level and y in level:
                    if level[x]!=level[y]:
                        return True
                    else:
                        return False
                if x in level or y in level:
                    return False