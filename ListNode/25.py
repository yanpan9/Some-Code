from data_structure import ListNode

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_N, dummy_O = ListNode(0), ListNode(0)
        dummy_O.next = head
        length, node = 0, head
        while node:
            length += 1
            node = node.next
        node_N = dummy_N
        for _ in range(length//k):
            tail = dummy_O.next
            for _ in range(k):
                node_O = dummy_O.next
                dummy_O.next = node_O.next
                node_O.next = node_N.next
                node_N.next = node_O
            node_N = tail
        node_N.next = dummy_O.next
        return dummy_N.next