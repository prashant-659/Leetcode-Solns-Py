class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}
        res=[]

        def comb(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in keyboard[digits[i]]:
                comb(i + 1, curStr + c)
        
        if digits:
            comb(0, "")
        
        return res




            



        

        