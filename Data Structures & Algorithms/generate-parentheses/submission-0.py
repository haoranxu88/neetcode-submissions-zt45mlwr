class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # keep track of n, while we backtrack we can choose to complete a parentheses from the stack or generate another parenthesis
        # n = 3
        # (( n = 1
        #   ((( n = 0   (() n = 1
        #   ((()))      (()( n = 0
        #               (()())
        # () n = 2
        #   ()( n = 1
        #       ()(()) n = 0    ()()() n = 0

        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append(''.join(stack))
                return

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()

            if openN > closedN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
            

