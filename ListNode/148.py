from data_structure import ListNode

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head:
            return self.mergeSort(head)
        else:
            return head
    
    def mergeSort(self, head: ListNode) -> ListNode:
        if head.next:
            slow, fast = head, head
            pre = None
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            pre.next = None
            left = self.mergeSort(head)
            right = self.mergeSort(slow)
            return self.mergeTwoLists(left, right)
        else:
            return head
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        node = dummy_head
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 if l1 else l2
        return dummy_head.next