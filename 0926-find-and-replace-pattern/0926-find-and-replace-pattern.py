class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def translate(pattern):
            trans = {}
            return tuple(trans.setdefault(c,len(trans)) for c in pattern)
            
        to_match = translate(pattern)
        return [word for word in words if to_match == translate(word)]