class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 not in nums:
            multi_all = 1
            for i in nums:
                multi_all *= i
            result = []
            for j in nums:
                result.append(int(multi_all/j))
            return result
        else:
            if nums.count(0) > 1:
                return [0]*len(nums)
            else:
                multi_all = 1
                for i in range(len(nums)):
                    if nums[i] != 0:
                        multi_all *= nums[i]
                    elif nums[i] == 0: decoy = i
                result = [0]*len(nums)
                result[decoy] = multi_all
                return result
        