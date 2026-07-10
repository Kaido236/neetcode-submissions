class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_lenght = 0
        left = 0
        has = {i:0 for i in s}
        for right in range(len(s)):
            has[s[right]] += 1
            store = (right - left + 1) - max(has.values())
            while store > k:
                has[s[left]] -= 1
                left += 1
                store = (right - left + 1) - max(has.values())
            distance = right - left + 1
            if distance > max_lenght:
                max_lenght = distance
        return max_lenght
        