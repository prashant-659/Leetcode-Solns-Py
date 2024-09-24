class Node:
    def __init__(self):
        self.edges={}
    
class Trie:

    def __init__(self):
        self.root=Node()

    def add(self,s):
        curr=self.root
        for c in s:
            if c not in curr.edges:
                curr.edges[c]=Node()
            curr=curr.edges[c]

    def search(self,s):
        curr=self.root
        count=0
        for c in s:
            if c not in curr.edges:
                return count
            count+=1 
            curr=curr.edges[c]
            
        return count

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        t=Trie()
        for x in arr1:
            t.add(str(x))

            longest=0
        for x in arr2:
            v=t.search(str(x))
            longest=max(longest,v)
        return longest
        
