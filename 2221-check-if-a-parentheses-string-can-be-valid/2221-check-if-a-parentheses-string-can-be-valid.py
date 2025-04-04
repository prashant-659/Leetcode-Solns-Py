class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        if len(s)%2==1:
            return False


        unlocked_cnt=0
        locked_cnt=0
        for i in range(len(s)):
            if locked[i]=="0":
                unlocked_cnt+=1
            elif s[i]=="(":
                locked_cnt+=1
            else:
                if locked_cnt:
                    locked_cnt-=1
                elif unlocked_cnt:
                    unlocked_cnt-=1
                else:
                    return False
        
        if locked_cnt==0:
            return True
        
        locked_cnt=0
        unlocked_cnt=0
        for i in reversed(range(len(s))):
            if locked[i]=="0":
                unlocked_cnt+=1
            elif s[i]==")":
                locked_cnt+=1
            else:
                if locked_cnt:
                    locked_cnt-=1
                elif unlocked_cnt:
                    unlocked_cnt-=1
                else:
                    return False
    
        return True 