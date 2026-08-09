class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        max_len = 0
        zeros = 0

        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        return max_len                

        