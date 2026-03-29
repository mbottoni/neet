class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        node       = head
        prev       = dummy  # separate pointer

        i = n
        while node:
            if i > 0:
                i -= 1
            else:
                prev = prev.next
            node  = node.next

        prev.next = prev.next.next
        return dummy.next  # return dummy.next, not head