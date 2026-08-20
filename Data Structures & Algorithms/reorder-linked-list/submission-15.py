# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find middle
        mid, fast = head, head.next
        while fast and fast.next:
            mid  = mid.next
            fast = fast.next.next

        # 2. Reverse second half
        second = mid.next
        prev   = None; mid.next = None    # None cuts the two halves 
        while second:
            temp         = second.next
            second.next  = prev
            prev         = second
            second       = temp

        # 3. Merge lists
        first, second = head, prev   # second is now None; take the previous element
        while second:
            temp1, temp2  = first.next, second.next
            first.next    = second
            second.next   = temp1
            first, second = temp1, temp2