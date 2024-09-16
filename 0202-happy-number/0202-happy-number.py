class Solution:
    def isHappy(self, n: int) -> bool:
    #     visit=set()
    #     while n not in visit:
    #         visit.add(n)
    #         n=self.sumofSquares(n)
    #         if n==1:
    #             return True
    #     return False

    # def sumofSquares(self, n: int) -> int:
    #     output=0
    #     while n:
    #         digit=n%10
    #         digit=digit ** 2
    #         output+=digit
    #         n=n//10
    #     return output

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1

            