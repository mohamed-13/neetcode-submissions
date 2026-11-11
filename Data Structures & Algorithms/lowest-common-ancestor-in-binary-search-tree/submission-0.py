# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        queue = [root]
        min_node,max_node = min(p.val,q.val),max(p.val,q.val)

        while queue:
            node = queue.pop(0)

            if min_node <= node.val and max_node >= node.val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            