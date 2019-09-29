class Solution_BF:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            lst = list()
            self.inOrderTraverse(root, lst)
            dic = {j:i for i,j in enumerate(lst)}
            p,q = dic[p.val], dic[q.val]
            while True:
                key = dic[root.val]
                if p<key and q<key:
                    root = root.left
                elif p>key and q>key:
                    root = root.right
                else:
                    return root
        else:
            return None
        
    def inOrderTraverse(self, root, lst):
        if root.left:
            self.inOrderTraverse(root.left, lst)
        lst.append(root.val)
        if root.right:
            self.inOrderTraverse(root.right, lst)