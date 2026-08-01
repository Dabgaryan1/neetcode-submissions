# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(node):
            if not node:
                return 0
            leftHeight = 1 + dfs(node.left)
            rightHeight = 1 + dfs(node.right)
            if abs(leftHeight - rightHeight) > 1:
                self.balanced = False
            return max(leftHeight, rightHeight)
            
        dfs(root)

        return self.balanced