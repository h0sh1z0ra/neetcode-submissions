# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        # While both are not null
        while list1 and list2:
            if list1.val < list2.val: # Compare the two current values
                tail.next = list1     
                list1 = list1.next    # walk list pointer forward
            
            else:
                tail.next = list2
                list2 = list2.next

            # tail.next is changed in the if statements above; update current
            tail = tail.next

        # tail.next is whatever isn't none
        tail.next = list1 or list2
        
        # dummy.next is the actual head; dummy is a "fake (w)anchor"
        head = dummy.next
        return head