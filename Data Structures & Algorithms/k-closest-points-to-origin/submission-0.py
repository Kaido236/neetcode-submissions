class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sums = []
        for i in points:
            sums.append(i[0]**2+i[1]**2)

        def min_heap(arr,n,i):
            smallest = i
            left = 2*i+1
            right = 2*i + 2

            if left < n and arr[left] < arr[smallest]:
                smallest = left
            if right < n and arr[right] < arr[smallest]:
                smallest = right
            
            if smallest != i:
                arr[i], arr[smallest] = arr[smallest],arr[i]
                points[i], points[smallest] = points[smallest],points[i]
                min_heap(arr,n,smallest)
        
        def build_min_heap(arr):
            n = len(arr)
            start = n//2
            for i in range(start,-1,-1):
                min_heap(arr,n,i)

        build_min_heap(sums)
        result = []
        for i in range(k):
            min_sum = sums[0]
            min_point = points[0]
            sums[0],sums[-1] = sums[-1],sums[0]
            points[0],points[-1] = points[-1],points[0]
            sums.pop()
            points.pop()
            result.append(min_point)
            min_heap(sums,len(sums),0)
        return result