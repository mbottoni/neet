class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()

        for i in range(len(lists)):
            list1 = lists[i]
            list2 = dummy.next
            curr = dummy
            
            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            
            if list1:
                curr.next = list1
            if list2:
                curr.next = list2

        return dummy.next