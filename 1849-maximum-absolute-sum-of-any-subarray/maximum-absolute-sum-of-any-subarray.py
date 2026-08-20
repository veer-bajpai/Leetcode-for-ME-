class Solution(object):
    def maxAbsoluteSum(self, nums):
        max_sum = 0
        min_sum = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            min_sum = min(min_sum, curr_sum)

        return max_sum - min_sum      
        