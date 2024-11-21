class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split(" ")
        mp=defaultdict(str)
        for w in words:
            mp[w[-1]]=w[:len(w)-1]
        word=[]
        for j in sorted(mp):
            word.append(mp[j])
        return " ".join(word)

