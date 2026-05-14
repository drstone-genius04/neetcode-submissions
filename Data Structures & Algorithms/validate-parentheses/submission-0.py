class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        res={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for c in s:
            if c in res:
                if stack and stack[-1]==res[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

            
        