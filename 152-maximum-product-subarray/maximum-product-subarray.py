class Solution(object):
    def maxProduct(self, nums):
        min_ending = nums[0]
        max_ending = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            possible_1 = curr
            possible_2 = max_ending * curr
            possible_3 = min_ending * curr

            max_ending = max(possible_1, possible_2, possible_3) 
            min_ending = min(possible_1, possible_2, possible_3)

            res = max(res, max_ending)
        return res    

        