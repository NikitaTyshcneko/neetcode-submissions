class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0: return False
        stack = []
        parentheses = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif (parentheses.get(i) not in stack) or (parentheses.get(i) != stack.pop()):
                return False
        return len(stack) == 0
        