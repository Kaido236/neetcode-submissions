import math
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = sum(nums) - sum(set(nums))
        for i in range(1,math.ceil(s)+1):
            if ((len(nums)- 1 - s//i) >= 0) and ((s//i - 1 >= 0)):
                if nums.count(s//i) > 1:
                    return s//i
        