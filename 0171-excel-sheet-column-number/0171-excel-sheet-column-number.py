class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col=0
        for char in columnTitle:
            col=col*26+(ord(char)-64)
        return col