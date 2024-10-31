class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        list1=['a','b','c','d','e','f','g','h']
        cord=0
        for i in range(len(list1)):
            if list1[i]==coordinates[0]:
                cord=i+1
        return False if (cord+int(coordinates[1]))%2==0 else True
