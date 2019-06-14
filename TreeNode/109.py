from data_structure import ListNode, TreeNode

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        elif not head.next:
            return TreeNode(head.val)
        else:
            slow = fast = head
            pre = None
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            node = TreeNode(slow.val)
            pre.next = None
            node.left = self.sortedListToBST(head)
            node.right = self.sortedListToBST(slow.next)
            return node