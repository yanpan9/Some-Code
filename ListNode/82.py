from data_structure import ListNode

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        pre, cur = dummy, head
        while cur and cur.next:
            if cur.val==cur.next.val:
                node = cur.next.next
                while node and node.val==cur.val:
                    node = node.next
                pre.next = node
                cur = node
            else:
                pre, cur = cur, cur.next
        return dummy.next