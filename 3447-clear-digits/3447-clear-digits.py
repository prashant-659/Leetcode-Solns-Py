class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[s[0]]
        if s[0].isdigit():
            stack.pop()

        for i in range(1,len(s)):
            if stack and s[i].isdigit():
                stack.pop()

            
            else:   
                stack.append(s[i])
        return "".join(stack)
                
