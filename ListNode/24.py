from data_structure import ListNode

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = ListNode(None)
        cur.next = head
        head = cur
        while True:
            if cur.next:
                node_1 = cur.next
                if node_1.next:
                    node_2 = node_1.next
                    cur.next = node_2
                    node_1.next = node_2.next
                    node_2.next = node_1
                    cur = node_1
                else:
                    break
            else:
                break
        return head.next