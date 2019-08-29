from data_structure import ListNode

class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy1, dummy2 = ListNode(None), ListNode(None)
        dummy1.next = head
        slow = fast = dummy1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        while cur:
            node = cur.next
            cur.next = dummy2.next
            dummy2.next = cur
            cur = node
        slow, fast = dummy1, dummy2
        while slow and fast:
            if slow.val==fast.val:
                slow = slow.next
                fast = fast.next
            else:
                return False
        else:
            return True