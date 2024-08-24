class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        # Convert the input string into a list of characters
        lst = list(s)
        
        # Iterate through the list with a step size of 2k
        for i in range(0, len(lst), k + k):
            # Reverse the sublist of characters within the range of i to i + k
            lst[i:k + i] = reversed(lst[i:k + i])
            
        # Join the reversed list of characters back into a string and return it
        return "".join(lst)
        
                                                                                                                                                                                                                                                                                                       
            


            