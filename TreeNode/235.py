from data_structure import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            return self.findAncestor(root, p.val, q.val)
        else:
            return None
    
    def findAncestor(self, root, p, q):
        val = root.val
        if p<val and q<val:
            return self.findAncestor(root.left, p, q)
        elif p>val and q>val:
            return self.findAncestor(root.right, p, q)
        else:
            return root