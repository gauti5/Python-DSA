# leetcode -> 150

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                b=stack.pop()
                a=stack.pop()

                if token=='+':
                    stack.append(a+b)
                elif token=='-':
                    stack.append(a-b)
                elif token=='*':
                    stack.append(a*b)
                else:
                    cal=int(a/b) if a*b>0 else -(-a//b)
                    stack.append(cal)
        return stack[0]
            