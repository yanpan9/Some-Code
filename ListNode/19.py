from data_structure import ListNode

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_1, node_2 = ListNode(None), head
        node_1.next = head
        head = node_1
        for i in range(1,n):
            node_2 = node_2.next
        while node_2.next:
            node_1 = node_1.next
            node_2 = node_2.next
        node_1.next = node_1.next.next
            
        return head.next