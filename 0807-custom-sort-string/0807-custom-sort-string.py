class Solution:
    def customSortString(self, order: str, s: str) -> str:
        new=[]
        c=Counter(s)
        
        for char in order:
            if char in s:
                while c[char]>0:
                    new.append(char)
                    c[char]-=1
                    if c[char]==0:
                        del c[char]

        newset=set(new)
        for char in s:
            if char not in newset:
                new.append(char)
        return "".join(new)
        
                
                

                
