class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count=Counter(nums)
        max_f=0
        for frequency in count.values():
            max_f=max(max_f,frequency)

        f_of_max_f=0
        for f in count.values():
            if f==max_f:
                f_of_max_f+=1

        return f_of_max_f*max_f
