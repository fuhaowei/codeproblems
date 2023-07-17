# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        cur1 = list1
        cur2 = list2
        head = None

        if not cur1 and not cur2:
            return None

        if cur1 and not cur2:
            return cur1

        if cur2 and not cur1:
            return cur2

        if cur1.val <= cur2.val:
            head = cur1
            cur1 = cur1.next
        
        elif cur2.val < cur1.val:
            head = cur2
            cur2 = cur2.next


        start = head
            
        while cur1 and cur2:
            if cur1.val < cur2.val:
                head.next = cur1
                head = head.next
                cur1 = cur1.next

            elif cur2.val < cur1.val:
                head.next = cur2
                head = head.next
                cur2 = cur2.next

            else:
                head.next = cur1
                head = head.next
                cur1 = cur1.next
                head.next = cur2
                head = head.next
                cur2 = cur2.next

        if cur1 and not cur2:
            head.next = cur1

        if cur2 and not cur1:
            head.next = cur2

        return start

                

                



