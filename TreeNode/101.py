from data_structure import TreeNode

class Solution_Recur:
    def isMirror(self, p, q):
        if not(p or q):
            return True
        elif bool(p) ^ bool(q):
            return False
        else:
            return ((p.val == q.val) and 
                    self.isMirror(p.left, q.right) and 
                    self.isMirror(p.right, q.left))
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.isMirror(root.left, root.right)

class Solution_Iter:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]
        while len(queue)>0:
            p, q = queue.pop(0), queue.pop(0)
            if (not p) and (not q):
                continue
            elif bool(p) ^ bool(q):
                return False
            elif p.val != q.val:
                return False
            else:
                queue.extend([p.left, q.right, p.right, q.left])
        return True