class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next

        n = len(stack) // 2

        swap_stack = []
        for i in range(n):
            swap_stack.append(stack[i])
            swap_stack.append(stack[-i - 1])

        if len(stack) % 2 == 1:
            swap_stack.append(stack[n])

        # Relink all at once at the end
        for i in range(len(swap_stack) - 1):
            swap_stack[i].next = swap_stack[i + 1]
        swap_stack[-1].next = None  # terminate the list