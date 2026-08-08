class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        last_index = {}
        max_len = 0

        for right, char in enumerate(s):
            if char in last_index and last_index[char] >= left:
                left = last_index[char] + 1

            last_index[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len               