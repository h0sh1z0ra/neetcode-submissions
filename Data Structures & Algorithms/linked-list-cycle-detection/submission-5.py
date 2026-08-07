# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # Need to guard against the none type for the jump
        # fast.next can't be None, but fast.next.next can
        while fast and fast.next:
            slow = slow.next      # jump once
            fast = fast.next.next # double jump

            # use "is" to compare nodes; == for values
            if slow is fast:
                return True
        
        return False