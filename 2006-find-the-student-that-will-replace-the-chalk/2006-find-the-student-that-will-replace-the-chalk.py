# class Solution:
#     def chalkReplacer(self, chalk: List[int], k: int) -> int:
#         # chalk_sum=0
#         # for i in range(len(chalk)):
#         #     chalk_sum+=chalk[i]
#         #     if chalk_sum>k:
#         #         break
#         # new_k=k%chalk_sum
#         # for i in range(len(chalk)):
#         #     if new_k<chalk[i]:
#         #         return i
#         #     else:
#         #         new_k-=chalk[i]
#         # return 0
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)

        prefix_sum = [0] * n
        prefix_sum[0] = chalk[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + chalk[i]

        sum_chalk = prefix_sum[n - 1]
        remaining_chalk = k % sum_chalk

        return self.__binary_search(prefix_sum, remaining_chalk)

    def __binary_search(self, arr, tar):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = low + (high - low) // 2

            if arr[mid] <= tar:
                low = mid + 1
            else:
                high = mid

        return high
            