from data_structure import ListNode

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                while not head is slow:
                    head = head.next
                    slow = slow.next
                else:
                    return head
        else:
            return None