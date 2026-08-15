# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #     # Find the longest walk, with the turning point being this node, so
    #     # find the length of left and right nodes from each node
    #     if not root:
    #         return 0
        
    #     leftHeight = self.maxHeight(root.left)
    #     rightHeight = self.maxHeight(root.right)
    #     diameter = leftHeight + rightHeight

    #     maxDiameter = max(self.diameterOfBinaryTree(root.left),                   
    #               self.diameterOfBinaryTree(root.right))

    #     return max(maxDiameter, diameter)


    # # Brute force via recursion
    # def maxHeight(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
        
    #     return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

        # dfs
        if not root:
            return None
            
        stack   = [root]
        nodeMap = {None: (0,0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in nodeMap:
                stack.append(node.left)
            elif node.right and node.right not in nodeMap:
                stack.append(node.right)

            # End of branch
            else:
                node = stack.pop()
            
                lH, lD = nodeMap[node.left]
                rH, rD = nodeMap[node.right]

                nodeMap[node] = (1 + max(lH, rH), max(lH+rH, lD, rD))
            
        return nodeMap[root][1]


