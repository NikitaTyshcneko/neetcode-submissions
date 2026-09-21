class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        parenthesis = []
        
        def dfs(open_p, close_p):
            if open_p == close_p == n:
                parenthesis.append(''.join(stack))

            if open_p < n:
                stack.append('(')
                dfs(open_p+1, close_p)
                stack.pop()
            if close_p < open_p:
                stack.append(')')
                dfs(open_p, close_p+1)
                stack.pop()
        
        dfs(0, 0)

        return parenthesis

        