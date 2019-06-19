from data_structure import TreeNode
from collections import deque

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root:
            sub_set = {-1,0,1}
            flag = self.maxDepth(root.left)-self.maxDepth(root.right) in sub_set
            return flag and self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return True
    
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