class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = list()
        def dfs(lst):
            node = lst[-1]
            if not (node.left or node.right):
                res.append("->".join([str(i.val) for i in lst]))
            else:
                for child in [node.left, node.right]:
                    if child:
                        lst.append(child)
                        dfs(lst)
                        lst.pop()
        if root:
            dfs([root])
        return res