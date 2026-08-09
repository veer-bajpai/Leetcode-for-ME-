class Solution(object):
    def characterReplacement(self, s, k):
        counts = {}
        max_len = 0
        left = 0
        
        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            
            if max_len + 1 - max(counts.values()) <= k:
                max_len += 1
            else:
                counts[s[left]] -= 1
                left += 1
        
        return max_len