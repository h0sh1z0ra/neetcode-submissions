# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #BFS
        pQ, qQ = deque([p]), deque([q])
        
        while pQ and qQ:
            for _ in range(len(pQ)):
                nodeP = pQ.popleft()
                nodeQ = qQ.popleft()
                
                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                pQ.append(nodeP.left)
                pQ.append(nodeP.right)
                qQ.append(nodeQ.left)            
                qQ.append(nodeQ.right)

        return True