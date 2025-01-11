import re

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        return re.search(p.replace("*","(.*)"), s) is not None