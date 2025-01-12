class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        if len(s)%2==1:
            return False


        unlocked=[]
        stack_locked=[]
        for i in range(len(s)):
            if locked[i]=="0":
                unlocked.append(i)
            elif s[i]=="(":
                stack_locked.append(i)
            else:
                if stack_locked:
                    stack_locked.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        while stack_locked and unlocked and stack_locked[-1]<unlocked[-1]:
            stack_locked.pop()
            unlocked.pop()
        
        if stack_locked:
            return False
        return True 