from data_structure import ListNode

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if cur.val == val:
                cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return dummy.next