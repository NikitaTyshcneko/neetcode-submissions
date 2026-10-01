# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        result = []
        queue = collections.deque([root])

        while queue:
            is_shown = False
            for _ in range(len(queue)):
                node = queue.popleft()
                if not is_shown and node is not None:
                    result.append(node.val)
                    is_shown = True
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return result
            
        