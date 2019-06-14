from data_structure import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return list()
        else:
            result = list()
            level = [root]
            while len(level):
                result.append([node.val for node in level])
                new_level = list()
                for node in level:
                    for child in (node.left, node.right):
                        if child:
                            new_level.append(child)
                level = new_level
            return result