class Solution:
    def jump(self, nums: List[int]) -> int:

        count = 1
        queue = collections.deque([0])
        visited = set()

        while queue:
            print(queue)
            for _ in range(len(queue)):
                current_index = queue.popleft()
                value = nums[current_index]
                for j in range(1, value+1):
                    if current_index+j not in visited:
                        if current_index+j == len(nums)-1:
                            return count
                        if current_index+j >len(nums)-1:
                            break
                        queue.append(current_index+j)
                        visited.add(current_index+j)
            count += 1
        
        return 0
        