# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        stack = []
        while node:
            stack.append(node.val)
            node = node.next
        
        n = len(stack)
        stack2 = []
        for i in range(0, len(stack), k):
            chunk = stack[i:i+k]
            if len(chunk)==k:
                chunk = chunk[::-1]
            else:
                pass
            stack2 = stack2 + chunk

        dummy = ListNode()
        init = dummy
        print(stack2)
        for i in range(len(stack2)):
            if i<len(stack2)-1:
                dummy.next = ListNode()
                dummy.val = stack2[i]
                dummy = dummy.next
            else:
                dummy.val = stack2[i]
                dummy = dummy.next

        return init
        