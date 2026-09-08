# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        res = [root.val]

        while q:
            curLvl = []
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.right:
                    q.append(node.right)
                    curLvl.append(node.right.val)
                    
                
                if node.left:
                    q.append(node.left)
                    curLvl.append(node.left.val)
                    
            if curLvl:
                res.append(curLvl[0])
        
        return res
                