from data_structure import ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        pos = head
        while l1 and l2:
            if l1.val>=l2.val:
                pos.next = l2
                l2 = l2.next
            else:
                pos.next = l1
                l1 = l1.next
            pos = pos.next
        if l1:
            pos.next = l1
        elif l2:
            pos.next = l2
        
        return head.next