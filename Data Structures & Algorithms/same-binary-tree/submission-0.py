# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Initialize stack with both root nodes as a pair
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            # If both nodes are None, this path is valid; move to next items
            if not node1 and not node2:
                continue
            
            # If one is None but the other isn't, or their values mismatch
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Push matching child pairs onto the stack as single tuples
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True
