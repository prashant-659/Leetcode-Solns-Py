class Node:
    def __init__(self):
        self.children={}
        self.score=0
class Trie:
    def __init__(self):
        self.root=Node()
    
    def add(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=Node()
            node=node.children[char]
            node.score+=1

    def count(self,word):
        node=self.root
        ans=0
        for char in word:
            ans+=node.children[char].score
            node=node.children[char]
        return ans    


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie=Trie()
        res=[]
        for w in words:
            trie.add(w)
        for w in words:
            res.append(trie.count(w))
        return res

        