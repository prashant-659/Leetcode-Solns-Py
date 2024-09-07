class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if digits[-1] == 9:
        #     if len(digits) == 1:  # Already a 9
        #         return [1, 0]
        #     return self.plusOne(digits[:-1]) + [0]
        # else:
        #     digits[-1] += 1
        # return digits

        one=1
        i=0
        digits=digits[::-1]

        while one:
            if i<len(digits):
                if digits[i]==9:
                    digits[i]=0
                else: 
                    digits[i]+=1
                    one=0
            else:
                digits.append(1)
                one=0
            i+=1
        return digits[::-1]