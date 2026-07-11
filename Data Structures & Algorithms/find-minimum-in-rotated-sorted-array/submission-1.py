class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return nums[0]
        if not nums:
            return 
        left = 0
        right = len(nums)-1
        border_left = nums[0]
        border_right = nums[-1]
        while left<right:
            mid  = (left+right)//2
            if nums[mid] <= nums[mid+1]:
                if nums[mid] >= border_left:
                    left = mid+1
                if nums[mid] <= border_right:
                    right = mid
            elif nums[mid] > nums[mid+1]:
                return nums[mid+1]
        