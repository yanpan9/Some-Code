from data_structure import TreeNode

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            stack = [root]
            dummy = TreeNode(None)
            cur = dummy
            while stack:
                node = stack.pop()
                cur.right = node
                cur = node
                for c in (node.right, node.left):
                    if c:
                        stack.append(c)
                cur.left = None