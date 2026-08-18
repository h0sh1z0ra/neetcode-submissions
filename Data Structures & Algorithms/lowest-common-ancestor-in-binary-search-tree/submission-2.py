# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Start at top
        cur = root

        # Note that this tree is kinda sorted. Left of a node is smaller,
        # right of a node is larger than the current value.
        while cur:
            # if both nodes are larger than the current, it might be a 
            # right subnode
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # if both nodes smaller than currnet, must be left subnode
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # if it's a split, or indeed the actual ancestor, just return cur
            else:
                return cur