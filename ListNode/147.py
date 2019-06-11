from data_structure import ListNode

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        head_n = ListNode(float("-inf"))
        while head:
            n_1, n_2 = head_n, head_n.next
            while n_2:
                if head.val<n_2.val:
                    n_1.next = head
                    head = head.next
                    n_1.next.next = n_2
                    break
                else:
                    n_1 = n_2
                    n_2 = n_2.next
            else:
                n_1.next = head
                head = head.next
                n_1.next.next = None
        return head_n.next