from data_structure import TreeNode

class Solution_Recursion:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return list()
        if root.left:
            res = self.inorderTraversal(root.left)
        else:
            res = list()
        res.append(root.val)
        if root.right:
            res.extend(self.inorderTraversal(root.right))
        return res

class Solution_Stack:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = list(), list()
        cur = root
        while(cur or (len(stack)!=0)):
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop(-1)
                res.append(cur.val)
                cur = cur.right
        return res