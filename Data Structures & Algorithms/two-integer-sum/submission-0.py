class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_count = {}
        for i in range(len(nums)):
            temp = target - nums[i]
    
            if nums[i] in hash_count:
                return [hash_count[nums[i]],i]
                
            if temp not in hash_count:
                hash_count[temp] = i
        