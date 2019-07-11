from data_structure import ListNode

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        i = 1
        head = dummy
        while i<m:
            head = head.next
            i += 1
        node = head.next
        while i<n:
            node = node.next
            i+=1
        tail = node.next
        node.next = None
        node = head.next
        head.next = tail
        while node:
            temp = node.next
            node.next = head.next
            head.next = node
            node = temp
        return dummy.next

class Solution_LeetCode:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        prev, cur = dummy, head
        i = 1
        while i<m:
            prev, cur = cur, cur.next
            i += 1
        head, tail = prev, cur
        while i<=n:
            next_node = cur.next
            cur.next = prev
            prev, cur = cur, next_node
            i += 1
        head.next = prev
        tail.next = cur
        return dummy.next