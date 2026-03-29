# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        vis = set()
        while node:
            if node in vis:
                return True
            else:
                vis.add(node)
            node = node.next

        return False
        