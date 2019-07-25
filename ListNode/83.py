from data_structure import ListNode

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            cur = head
            while cur.next:
                if cur.val == cur.next.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
        return head