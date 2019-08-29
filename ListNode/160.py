from data_structure import ListNode

class Solution_HS(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nset = set()
        cur = headA
        while cur:
            nset.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in nset:
                return cur
            else:
                cur = cur.next
        else:
            return None

class Solution_DouPon(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        c1, c2 = headA, headB
        while c1 != c2:
            if c1:
                c1 = c1.next
            else:
                c1 = headB
            if c2:
                c2 = c2.next
            else:
                c2 = headA
        return c1