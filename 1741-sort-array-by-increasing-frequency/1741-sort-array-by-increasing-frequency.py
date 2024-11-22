class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ct=Counter(nums).most_common()
        ct.sort(key=lambda x:x[0], reverse=True)
        ct.sort(key=lambda x:x[1])
        ans=[]
        for i in ct:
            a,b=i
            ans.extend([a]*b)
        return ans
