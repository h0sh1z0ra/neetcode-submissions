"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head

        seen = {}
        seen[None] = None

        while cur:
            seen[cur] = Node(cur.val)
            cur = cur.next
        cur = head

        # Once hashmap is initialised, you can index it with the random and nexts
        while cur:
            copy = seen[cur]
            copy.next = seen[cur.next]
            copy.random = seen[cur.random]
            cur = cur.next

        return seen[head]