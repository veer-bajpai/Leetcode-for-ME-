class Solution(object):
    def minSubArrayLen(self, target, nums):
        low = 0
        res = 0
        min_len = float('inf')

        for high in range(len(nums)):
            res += nums[high]

            while res >= target:
                min_len = min(min_len, high - low + 1)
                res -= nums[low]
                low += 1
        return 0 if min_len == float('inf') else min_len        
        