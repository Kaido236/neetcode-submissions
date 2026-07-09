class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set_father = {i:i-1 for i in set(nums)}
        set_count = {} 
        for i in nums:
            set_count[i-1] = 0
            set_count[i] = 0
            set_count[i+1] = 0

        for e in set(nums):
            set_father[e] = self.find_father(set_father,e)
        for i in set_father:
            set_count[set_father[i]] += 1
        return max(set_count.values())
    
    def find_father(self,set_father,a):
        if set_father[a] in set_father:
            set_father[a] = self.find_father(set_father,set_father[a])
        return set_father[a]
        