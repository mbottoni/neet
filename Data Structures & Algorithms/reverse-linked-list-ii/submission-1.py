class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = head
        i = 1
        vals = []
        while node:
            if left <= i <= right:
                vals.append(node.val)
            node = node.next
            i += 1

        node = head
        i = 1
        while node:
            if left <= i <= right:
                node.val = vals.pop()
            node = node.next
            i += 1

        return head