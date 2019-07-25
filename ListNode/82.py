from data_structure import ListNode

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            node = cur.next
            if node.val==node.next.val:
                val = node.val
                while node and node.val==val:
                    node = node.next
                cur.next = node
            else:
                cur = cur.next
        return dummy.next