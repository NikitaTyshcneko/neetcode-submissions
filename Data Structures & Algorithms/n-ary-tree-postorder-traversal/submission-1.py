"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return[]
        result = []
        for i in root.children:
            result.extend(self.postorder(i))
        
        result.append(root.val)

        return result
        



        