from data_structure import TreeNode
from collections import deque

class Solution_DouPon_Rec:
    # TLE
    def findTarget(self, root: TreeNode, k: int) -> bool:
        return self.douPointer(root, root, k)
                
    def douPointer(self, low, high, k):
        if low==high:
            if low.val+high.val>k:
                if low.left:
                    return self.douPointer(low.left, high, k)
            elif high.right:
                return self.douPointer(low, high.right, k)
        else:
            if low.val+high.val>k:
                l = h = False
                if low.left:
                    l = self.douPointer(low.left, high, k)
                if high.left:
                    h = self.douPointer(low, high.left, k)
                return l or h
            elif low.val+high.val<k:
                l = h = False
                if low.right:
                    l = self.douPointer(low.right, high, k)
                if high.right:
                    h = self.douPointer(low, high.right, k)
                return l or h
            else:
                return True

class Solution_HashSet:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        hs = set()
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if k -node.val in hs:
                return True
            else:
                hs.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            return False