class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        # n = len(nums)
        # res = []
        # for i in range(n):
        #     res.append(nums[i] - i) #finding the sslope

        # a = Counter(res) #good pairs hashmap
        # ans = n * (n - 1) // 2
        # for x in a:
        #     if a[x] > 1:
        #         ans -= a[x] * (a[x] - 1) // 2
        
        # return ans

        good_pairs=0
        total_pairs=0
        ct=defaultdict(int)
        for i in range(len(nums)):
            total_pairs+=i
            good_pairs+=ct[nums[i]-i]
            ct[nums[i]-i]+=1



        return total_pairs-good_pairs
