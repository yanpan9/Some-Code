from data_structure import RandomListNode as Node 

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head:
            node_dict = dict()
            cur = head
            while cur:
                if cur not in node_dict:
                    node = Node(cur.val, None, None)
                    node_dict[cur]=node
                cur = cur.next
            cur = head
            while cur:
                if cur.next:
                    node_dict[cur].next = node_dict[cur.next]
                if cur.random:
                    node_dict[cur].random = node_dict[cur.random]
                cur = cur.next
            return node_dict[head]
        else:
            return None