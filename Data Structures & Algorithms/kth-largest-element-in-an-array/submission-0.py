class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def max_heap(arr,n,i):
            largest = i
            left = 2*i + 1
            right = 2*i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i],arr[largest] = arr[largest],arr[i]
                max_heap(arr,n,largest)
            
        def built_max_heap(arr):
            n = len(arr)
            start = n//2
            for i in range(start,-1,-1):
               max_heap(arr,n,i)

        built_max_heap(nums)
        max_current = 0
        for i in range(k):
            max_current = nums[0]
            nums[0],nums[-1] = nums[-1],nums[0]
            nums.pop()
            max_heap(nums,len(nums),0)
        return max_current