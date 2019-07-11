from data_structure import ListNode

class Solution_DoublePoint:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        node,length = head,0
        while node:
            length += 1
            node = node.next
        if length<=1:
            return head
        else:
            k = k%length
            fast,i = head,0
            while i<k:
                fast=fast.next
                i += 1
            slow = head
            while fast.next:
                slow, fast = slow.next, fast.next
                i += 1
            fast.next = head
            head = slow.next
            slow.next = None
            return head

