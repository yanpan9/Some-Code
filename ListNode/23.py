from data_structure import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        def adjustHeap(lists, i, length):
            temp = lists[i]
            k = 2*i+1
            while k < length:
                if k+1 < length and lists[k].val>lists[k+1].val:
                    k+=1
                if temp.val > lists[k].val:
                    lists[i]=lists[k]
                    i=k
                else:
                    break
                k = 2*k+1
            lists[i]=temp
        head = ListNode(None)
        cur = head
        lists = [elem for elem in lists if elem]
        length = len(lists)
        for i in range(length//2-1, -1, -1):
            adjustHeap(lists, i, length)
        while length>1:
            cur.next = lists[0]
            cur = cur.next
            lists[0]=lists[0].next
            if not lists[0]:
                lists[0]=lists[length-1]
                length-=1
            adjustHeap(lists, 0, length)
        if len(lists)==0:
            return None
        else:
            cur.next = lists[0]
            return head.next
            