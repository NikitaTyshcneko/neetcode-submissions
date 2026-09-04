class MyQueue:

    def __init__(self):
        self.array = []
        self.start_position = 0
        

    def push(self, x: int) -> None:
        self.array.append(x)
        

    def pop(self) -> int:
        self.start_position += 1
        return self.array[self.start_position-1]
        

    def peek(self) -> int:
        return self.array[self.start_position]
        

    def empty(self) -> bool:
        return self.start_position == len(self.array)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()