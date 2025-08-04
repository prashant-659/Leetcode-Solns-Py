class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # l=0
        # maxi=-1
        # mp=defaultdict(int)
        # for r in range(len(fruits)):
        #     mp[fruits[r]]+=1
        #     if len(mp)>2:
        #         mp[fruits[l]]-=1
        #         if mp[l]==0:
        #             del mp[fruits[l]]
        #         l+=1
        #     maxi = max(maxi, r - l + 1)
        # return maxi
        l = 0
        maxi = -1
        mp = defaultdict(int)
        for r in range(len(fruits)):
            mp[fruits[r]] += 1
            while len(mp) > 2:
                mp[fruits[l]] -= 1
                if mp[fruits[l]] == 0:
                    del mp[fruits[l]]
                l += 1
            maxi = max(maxi, r - l + 1)
        return maxi