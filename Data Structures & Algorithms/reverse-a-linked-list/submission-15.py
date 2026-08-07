# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = head

            # Ends up none
            # Example starts from head of list
            while curr:
                temp = curr.next     # point to idx 1
                curr.next = prev     # points pointer backwards
                prev = curr          # advance prev forward
                curr = temp          # move curr forward

                # temp holds next, curr.next pointed to prev, prev = curr
                # curr = curr.next (temp)

            return prev

    