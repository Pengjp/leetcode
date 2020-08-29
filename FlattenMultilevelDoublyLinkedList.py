# FlattenMultilevelDoublyLinkedList.py
class Solution1:
    def flatten(self, head: 'Node') -> 'Node':

        if not head:
            return 
        
        stk=[head]
        prev=Node(0)
        
        while stk:
            root=stk.pop()
            root.prev=prev
            prev.next=root
            prev=root
            if root.next:
                stk.append(root.next)
            if root.child:
                stk.append(root.child)
                root.child=None
                
        head.prev=None
        return head

class Solution2:
    def flatten(self, head: 'Node') -> 'Node':
        h = head

        while h: # if head node is not empty or has not reached the end 
            if h.child: # if current node has a child
                right = h.next # grab the next to connect later 
                h.next = h.child # set next to its child to flatten
                h.next.prev = h # connect back
                h.child = None # set child to None
                p = h.next # grad child's next
                while p.next: # if this child level has more, just grab them all
                    p = p.next
                p.next = right # connect back
                if right: 
                    right.prev = p
            h = h.next # no child, just move on
        return head