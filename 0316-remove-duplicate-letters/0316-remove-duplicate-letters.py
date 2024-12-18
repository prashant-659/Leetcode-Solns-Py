class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq={ch:0 for ch in "abcdefghijklmnopqrstuvwxyz"}
        for ch  in s:
            freq[ch]+=1

        stack=[]
        seen=set()

        for ch in s:
            freq[ch]-=1
            if ch in seen:
                continue
            

            while stack and stack[-1]>ch and freq[stack[-1]]>0:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)