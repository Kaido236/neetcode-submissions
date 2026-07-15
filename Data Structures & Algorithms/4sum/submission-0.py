class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if sum(nums) == target and len(nums) == 4:
            return [nums]
        nums.sort()
        result = list()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l = j+1
                r = len(nums)-1
                const_sum = nums[i] + nums[j]
                while l<r:
                    dynamic_sum = const_sum + nums[l] + nums[r]
                    if dynamic_sum > target:
                        r -= 1
                    elif dynamic_sum < target:
                        l += 1
                    else:
                        if [nums[i],nums[j],nums[l],nums[r]] not in result:
                            result.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
        return result