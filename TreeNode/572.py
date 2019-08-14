from data_structure import TreeNode

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return False
        else:
            return self.hasSubtree(s,t)
        
    def isSametree(self, p, q):   
        if not (p or q):
            return True
        elif bool(p) ^ bool(q):
            return False
        else:
            return (p.val==q.val and 
                    self.isSametree(p.left, q.left) and 
                    self.isSametree(p.right, q.right)
                   )
        
    def hasSubtree(self, p, q):
        if not (p or q):
            return True
        elif bool(p) ^ bool(q):
            return False
        else:
            return (self.isSametree(p,q) or
                    self.hasSubtree(p.left, q) or 
                    self.hasSubtree(p.right, q))