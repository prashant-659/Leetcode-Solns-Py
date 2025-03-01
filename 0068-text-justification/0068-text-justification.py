# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         def findline(i, j,spacesPerSlot, extraspaces):
#             line=""
#             for k in range(j):
#                 line+=words[k]
#                 if k==j-1:
#                     break
#                 for z in range(1,spacesPerSlot+1 ):
#                     line+=" "
#                 if extraspaces>0:
#                     line+=" "
#                     extraspaces-=1
#             while len(line)<maxWidth:
#                 line+=" "

#         res=[]
#         n=len(words)
#         MAXWIDTH=maxWidth
#         i=0
#         lettersCount=len(words[i])
#         while i<n:
#             j=i+1
#             space=0
#             while j<n and len(words[j])+1+space+lettersCount<=maxWidth:
#                 lettersCount+=len(words[j])
#                 space+=1
#                 j+=1
#             remainSlots=maxWidth-lettersCount
#             spacesPerSlot=remainSlots//space if space!=0 else 0
#             extraspaces=remainSlots%space if space!=0 else 0
#             if j==n: #left justified
#                 spacesPerSlot=1
#                 extraspaces=0
#             res.append(findline(i,j,spacesPerSlot, extraspaces))

#             i=j
#         return res


from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def findline(i, j, spacesPerSlot, extraspaces, words):
            line = ""
            for k in range(i, j):
                line += words[k]
                if k == j - 1:
                    break
                for z in range(spacesPerSlot):
                    line += " "
                if extraspaces > 0:
                    line += " "
                    extraspaces -= 1
            while len(line) < maxWidth:
                line += " "
            return line
        
        res = []
        n = len(words)
        i = 0
        while i < n:
            j = i + 1
            lineLength = len(words[i])
            while j < n and lineLength + len(words[j]) + (j - i) <= maxWidth:
                lineLength += len(words[j])
                j += 1
            
            spacesBetweenWords = j - i - 1
            totalSpaces = maxWidth - lineLength
            
            if j == n or spacesBetweenWords == 0:
                # Left-justify the last line or when there's only one word in the line
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
                res.append(line)
            else:
                spacesPerSlot = totalSpaces // spacesBetweenWords
                extraspaces = totalSpaces % spacesBetweenWords
                res.append(findline(i, j, spacesPerSlot, extraspaces, words))
            
            i = j
        
        return res
