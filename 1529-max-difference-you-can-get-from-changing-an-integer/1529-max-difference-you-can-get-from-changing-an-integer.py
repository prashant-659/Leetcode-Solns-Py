class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        sMax = list(s)
        for ch in sMax:
            if ch != '9':
                target = ch
                break
        else:
            target = None
        if target:
            sMax = ['9' if c == target else c for c in sMax]
        sMin = list(s)
        if sMin[0] != '1':
            target = sMin[0]
            sMin = ['1' if c == target else c for c in sMin]
        else:
            target = None
            for ch in sMin[1:]:
                if ch not in ('0', '1'):
                    target = ch
                    break
            if target:
                sMin = ['0' if c == target else c for c in sMin]
        return int(''.join(sMax)) - int(''.join(sMin))