# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        if root:
            queue.append(root)

        level = 0

        while queue:
            for i in range(len(queue)):
                currNode = queue.popleft()  # Pop from left, since we append to right
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            
            level += 1
        
        return level

