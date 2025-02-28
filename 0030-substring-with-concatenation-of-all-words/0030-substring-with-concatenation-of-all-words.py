class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or  not s:
            return []

      
        word_length=len(words[0])
        total_length=word_length*len(words)
        want=Counter(words)

        res=[]
        for i in range(word_length):
            left=i
            count=0
            tempW_count={}
            for j in range(i, len(s)-word_length+1, word_length):
                word=s[j:j+word_length]
                if word in want:
                    tempW_count[word]=tempW_count.get(word,0)+1
                    count+=1

                    while tempW_count[word]>want[word]:
                        left_word=s[left:left+word_length]
                        tempW_count[left_word]-=1
                        left+=word_length
                        count-=1
                    if count==len(words):
                        res.append(left)
                else:
                    tempW_count.clear()
                    count=0
                    left=j+word_length
        return res
