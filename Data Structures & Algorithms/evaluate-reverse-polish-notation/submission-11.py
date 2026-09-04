class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation_map = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y,
            '/': lambda x, y: int(x/y),
        }

        stack = []

        for i in tokens:
            if operation_map.get(i):
                a = stack.pop()
                b = stack.pop()
                if (a == 0 or b == 0) and i == '/': stack.append(0)
                else:
                    total = operation_map.get(i)(b, a)
                    stack.append(total)
            else:
                stack.append(int(i))
        
        return int(stack[0])

        