# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curMax):
            if not node:
                return 0
            
            goodCount = 1 if node.val >= curMax else 0
            curMax = max(curMax, node.val)
            goodCount += dfs(node.left, curMax)
            goodCount += dfs(node.right, curMax)
            return goodCount
        
        return dfs(root, root.val)