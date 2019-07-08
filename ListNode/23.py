from data_structure import ListNode
from typing import List

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(None)
        cur = head
        self.lists = [elem for elem in lists if elem]
        self.length = len(self.lists)
        if self.length==0:
            return
        for i in range(self.length//2-1, -1, -1):
            self.adjustHeap(i)
        while self.length>1:
            cur.next = self.lists[0]
            cur = cur.next
            self.lists[0] = self.lists[0].next
            if not self.lists[0]:
                self.lists[0]=self.lists.pop()
                self.length -= 1
            self.adjustHeap(0)
        cur.next = self.lists[0]
        return head.next
        
    def adjustHeap(self, i):
        temp = self.lists[i]
        k = 2*i+1
        while k < self.length:
            if k+1 < self.length and self.lists[k].val>self.lists[k+1].val:
                k+=1
            if temp.val > self.lists[k].val:
                self.lists[i] = self.lists[k]
                i=k
            else:
                break
            k = 2*k+1
        self.lists[i]=temp

class Solution_LoserTree:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_node, max_node = ListNode(-2**32), ListNode(2**32-1)
        self.lists = [min_node]
        for ele in lists:
            self.lists.append(ele if ele else  max_node)
        self.length = len(lists)
        if not self.length:
            return
        else:
            dummy_head = ListNode(None)
            node = dummy_head
            for i in range(self.length):
                if not self.lists[i]:
                    self.lists[i]=max_node
        self.createLoserTree()
        
        while self.lists[self.loser_tree[0]]!=max_node:
            node.next = self.lists[self.loser_tree[0]]
            node = node.next
            if self.lists[self.loser_tree[0]].next:
                self.lists[self.loser_tree[0]] = self.lists[self.loser_tree[0]].next
            else:
                self.lists[self.loser_tree[0]] = max_node
            self.adjustTree(self.loser_tree[0])
        node.next = None
        return dummy_head.next
        
        
    def createLoserTree(self):
        self.loser_tree = [0 for _ in range(self.length)]
        for i in range(self.length, 0, -1):
            self.adjustTree(i)
            
    def adjustTree(self, leaf_idx):
        tree_idx = (self.length+leaf_idx-1)//2
        while tree_idx>0:
            if self.lists[leaf_idx].val>self.lists[self.loser_tree[tree_idx]].val:
                leaf_idx, self.loser_tree[tree_idx] = self.loser_tree[tree_idx], leaf_idx
            tree_idx = tree_idx//2
        self.loser_tree[0] = leaf_idx