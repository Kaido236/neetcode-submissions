class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nums = heights
        l,r = 0,len(nums)-1
        mmax = 0
        while l<r:
            distance = (r-l)
            if nums[l]<nums[r]:
                s = nums[l]*distance
                l+=1
            elif nums[l]>nums[r]:
                s = nums[r]*distance
                r-=1
            elif nums[l]==nums[r]:
                s = nums[r]*distance
                if nums[l+1] > nums[r-1]:
                    l += 1
                else:
                    r -= 1
            if s > mmax:
                    mmax = s
        return mmax