class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_up = s.upper()
        s_op = s.lower()
        s = ""
        sn = []
        for c in s_op:
            if c.isalnum():
                sn.append(c)
                s += c
        l = 0
        r = len(s)-1
        while l<r:
            temp = sn[l]
            sn[l] = sn[r]
            sn[r] = temp
            l += 1
            r -= 1
        return "".join(sn) == s
        