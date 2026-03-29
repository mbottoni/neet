class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        final = dummy
        node1 = l1
        node2 = l2
        carry = 0
        while node1 or node2 or carry:
            if not node1:
                node1_val = 0
            else:
                node1_val = node1.val
            
            if not node2:
                node2_val = 0
            else:
                node2_val = node2.val

            soma  = (node1_val + node2_val + carry) % 10
            carry = (node1_val + node2_val + carry) // 10

            x = ListNode()
            x.val = soma
            dummy.next = x
            dummy = dummy.next

            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None

        return final.next