class Solution:
    def arrangeWords(self, text: str) -> str:
        split=text.split(" ")
        split.sort(key=lambda x : len(x))
        ans=" ".join(split)
        ans=ans.capitalize()
        return ans