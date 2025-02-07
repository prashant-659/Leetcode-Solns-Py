class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s)!=len(t):
            return False
        visit=set()
        shift_ct=[0]*26
  
        for x,y in zip(s,t):
            if x==y:
                continue
            shift=(ord(y)-ord(x))%26
            shift_ct[shift]+=1
        for shift in range(1,26):
            max_need=(shift_ct[shift]-1)*26+shift
            if max_need>k:
                return False
            
            
        return True
            

        