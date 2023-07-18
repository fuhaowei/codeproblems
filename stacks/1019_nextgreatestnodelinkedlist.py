
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        ans = [0,0]
        stack = []
        actualidx = 1
        stack.append((head.val, actualidx))
        cur = head.next

        while cur:
            ans.append(0)
            #while there is stuff in the stack,
            #and the last value in the stack is smaller than the current node
            #pop it from the stack,  put it in ans

            while stack and stack[-1][0] < cur.val:
                val, idx = stack.pop()
                ans[idx] = cur.val

            actualidx += 1
            stack.append((cur.val, actualidx))
               

            #else, increase idx by 1, append new value and index in stack


            cur = cur.next

        return ans[1:]
