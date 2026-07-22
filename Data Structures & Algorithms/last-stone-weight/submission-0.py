class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def sink(arr,n,i):
            largest = i
            left = 2*i+1
            right = 2*i+2

            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest != i:
                arr[i],arr[largest] = arr[largest],arr[i]
                sink(arr,n,largest)
        
        def build_max_heap(arr):
            n = len(arr)
            start = n//2
            for i in range(start,-1,-1):
                sink(arr,n,i)
        
        def swim(arr,i):
            while i > 0:
                parent = (i-1)//2
                
                if arr[i] > arr[parent]:
                    arr[i],arr[parent] = arr[parent],arr[i]
                    i = parent
                else:
                    break
        
        build_max_heap(stones)
        n = len(stones)
        while len(stones) > 1:
            stone1 = stones[0]
            stones[0],stones[-1] = stones[-1],stones[0]
            stones.pop()
            sink(stones,len(stones),0)

            stone2 = stones[0]
            stones[0],stones[-1] = stones[-1],stones[0]
            stones.pop()
            sink(stones,len(stones),0)

            if stone2 < stone1:
                stones.append(abs(stone2 - stone1))
                swim(stones,len(stones)-1)

        if stones:
            return stones[0]
        else:
            return 0