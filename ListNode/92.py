from data_structure import ListNode

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        i = 1
        head = dummy
        while i<m:
            head = head.next
            i += 1
        node = head.next
        while i<n:
            node = node.next
            i+=1
        tail = node.next
        node.next = None
        node = head.next
        head.next = tail
        while node:
            temp = node.next
            node.next = head.next
            head.next = node
            node = temp
        return dummy.next