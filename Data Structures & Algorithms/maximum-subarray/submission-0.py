class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_local = float("-inf")
        max_global = float("-inf")
        for i in nums:
            max_local = max(max_local+i,i)
            max_global = max(max_local,max_global)
        return max_global
        
        