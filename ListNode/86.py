from data_structure import ListNode

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        d_l = ListNode(None)
        d_h = ListNode(None)
        n_l, n_h = d_l, d_h
        while head:
            if head.val < x:
                n_l.next = head
                n_l = n_l.next
            else:
                n_h.next = head
                n_h = n_h.next
            head = head.next
        n_l.next = d_h.next
        n_h.next = None
        return d_l.next