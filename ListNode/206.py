from data_structure import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        head_1, head_2 = ListNode(0), ListNode(0)
        head_1.next = head
        while head_1.next:
            node = head_1.next
            head_1.next = node.next
            node.next = head_2.next
            head_2.next = node
        return head_2.next