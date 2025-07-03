class Solution:
    def kthCharacter(self, k: int) -> str:
        word="a"
        while len(word)<k:
            gen_str=""
            for w in word:
                next_w=chr((ord(w)-ord('a')+1)%26 +ord('a'))
                gen_str+=next_w
            word+=gen_str
        return word[k-1]
