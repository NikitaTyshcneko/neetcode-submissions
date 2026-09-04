class MyStack:

    def __init__(self):
        self.array = deque()
        

    def push(self, x: int) -> None:
        self.array.append(x)
        for _ in range(len(self.array)-1):
            self.array.append(self.array.popleft())
        

    def pop(self) -> int:
        return self.array.popleft()

    def top(self) -> int:
        return self.array[0]
        

    def empty(self) -> bool:
        return len(self.array) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()