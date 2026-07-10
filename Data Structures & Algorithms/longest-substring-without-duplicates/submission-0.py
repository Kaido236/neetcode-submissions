class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        max_leight = 0
        left = 0
        hash_count = {i:-1 for i in s}
        for right in range(len(s)):
            if hash_count[s[right]] != -1:
                left = max(left,hash_count[s[right]] + 1)
                hash_count[s[right]] = right
            else:
                hash_count[s[right]] = right
            distance = right - left
            if max_leight < distance:
                max_leight = distance
        return max_leight+1
        