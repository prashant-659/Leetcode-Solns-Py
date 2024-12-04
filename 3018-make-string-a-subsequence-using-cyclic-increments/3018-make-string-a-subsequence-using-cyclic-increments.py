class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        letter_dict = {i: chr(96 + i) for i in range(1, 27)}
        if len(str2)>len(str1):
            return False
        str2set=set(str2)
        i=0
        j=0
        while i<len(str1) and j<len(str2):
            if ord(str1[i])==ord(str2[j]): 
            
                i+=1
                j+=1
            elif (ord(str1[i]) - ord('a') + 1) % 26 == (ord(str2[j]) - ord('a')):
                i+=1
                j+=1
            else:
                i+=1
            
        return len(str2)==j
        

