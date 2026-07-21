class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        strs = list("".join(map(str,nums)).split("0"))
        maxx = 0
        for i in strs:
            maxx = max(maxx,len(i))
        return maxx
