# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val
        def dfs(root):
            nonlocal result
            if root is None:
                return 0

            result_left = 0
            result_right = 0

            result_left = dfs(root.left)
            result_right = dfs(root.right)
            result_left = max(result_left, 0)
            result_right = max(result_right, 0)

            result = max(result, root.val + result_left + result_right)

            return root.val + max(result_left, result_right)
        dfs(root)
        return result
        
        