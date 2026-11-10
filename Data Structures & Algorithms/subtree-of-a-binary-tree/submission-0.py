# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSametree(p,q):
            stack = [(p,q)]

            while stack:
                n1,n2 = stack.pop()
                if not n1 and not n2:
                    continue
                
                if not n1 or not n2 or n1.val!=n2.val:
                    return False

                stack.append((n1.left,n2.left))
                stack.append((n1.right,n2.right))

            return True
        

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val == subRoot.val:
                    val = isSametree(node,subRoot)
                    if val:
                        return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
