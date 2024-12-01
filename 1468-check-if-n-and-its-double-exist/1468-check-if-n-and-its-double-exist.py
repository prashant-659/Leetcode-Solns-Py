class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        check=set()
        for i in range(len(arr)):
            if 2*arr[i] in check or (arr[i]%2==0 and arr[i]//2 in check):
                return True
            check.add(arr[i])
        return False
        
        