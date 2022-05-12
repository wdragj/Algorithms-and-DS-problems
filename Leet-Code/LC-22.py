# Medium

# Using global stack

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Add "(" open parenthesis if openC < n
        # Add ")" close parenthesis if closeC < openC
        # Valid parenthesis if openC == closeC == n
        
        stack = []
        res = []
        
        def backtrack(openC, closeC):
            if openC == closeC == n:
                res.append("".join(stack))
                return
            
            if openC < n: # Add "(" open parenthesis
                stack.append("(")
                backtrack(openC + 1, closeC)
                stack.pop()
                
            if closeC < openC: # Add ")" close parenthesis
                stack.append(")")
                backtrack(openC, closeC + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Add "(" open parenthesis if openC < n
        # Add ")" close parenthesis if closeC < openC
        # Valid parenthesis if openC == closeC == n
        
        res = []
        
        def backtrack(openC, closeC, parenthesis):
            if openC == closeC == n:
                res.append(parenthesis)
                return
            
            if openC < n: # Add "(", open parenthesis
                backtrack(openC + 1, closeC, parenthesis + "(")
            
            if closeC < openC: # Add ")", close parenthesis
                backtrack(openC, closeC + 1, parenthesis + ")")
        
        backtrack(0, 0, "")
        
        return res