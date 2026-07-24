class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2 = len(nums2)
        stack = []
        value_largest = [-1]*n2
        for i in range(n2):
            while stack and nums2[stack[-1]] < nums2[i]:
                pop_index = stack.pop()
                value_largest[pop_index] = nums2[i]
            stack.append(i)
        result = []
        hash_largest = {nums2[i]:value_largest[i] for i in range(n2)}
        for i in nums1:
            result.append(hash_largest[i])
        return result