# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            for i in range(len(queue1)):
                first_queue_node = queue1.popleft()
                second_queue_node = queue2.popleft()

                if first_queue_node is None and second_queue_node is None:
                    continue

                if first_queue_node is None or second_queue_node is None or first_queue_node.val != second_queue_node.val:
                    return False
                
                queue1.append(first_queue_node.right)
                queue1.append(first_queue_node.left)
                queue2.append(second_queue_node.right)
                queue2.append(second_queue_node.left)
        
        return queue1 == queue2
        