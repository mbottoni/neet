# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use stack
        s = []
        node = head
        node2 = head
        node3 = head
        while node:
            s.append(node.val)
            node = node.next
        




        i = 0 
        s = s[::-1]
        while node2:
            node2.val = s[i]
            i += 1
            node2 = node2.next

        return node3


        