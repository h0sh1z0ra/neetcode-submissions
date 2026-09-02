# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = [[root.val]]

        while q:
            lvl = []
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    lvl.append(node.left.val)

                if node.right:
                    q.append(node.right)
                    lvl.append(node.right.val)
            res.append(lvl)

        return res[:-1]
                
