class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def swimMax(self, arr, i):
        while i > 0:
            parent = (i - 1) // 2
            
            if arr[parent] < arr[i]:
                arr[parent], arr[i] = arr[i], arr[parent]
                i = parent
            else:
                break

    def swimMin(self, arr, i):
        while i > 0:
            parent = (i - 1) // 2
            
            if arr[parent] > arr[i]:
                arr[parent], arr[i] = arr[i], arr[parent]
                i = parent
            else:
                break

    def sinkMax(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[largest] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.sinkMax(arr, n, largest)

    def sinkMin(self, arr, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[smallest] > arr[left]:
            smallest = left
        if right < n and arr[smallest] > arr[right]:
            smallest = right
        
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.sinkMin(arr, n, smallest)        

    def addNum(self, num: int) -> None:
        self.maxHeap.append(num)
        self.swimMax(self.maxHeap, len(self.maxHeap) - 1)
        
        self.maxHeap[0], self.maxHeap[-1] = self.maxHeap[-1], self.maxHeap[0]
        self.minHeap.append(self.maxHeap.pop())

        if self.maxHeap:
            self.sinkMax(self.maxHeap, len(self.maxHeap), 0)
        self.swimMin(self.minHeap, len(self.minHeap) - 1)
        
        if len(self.minHeap) > len(self.maxHeap):
            self.minHeap[0], self.minHeap[-1] = self.minHeap[-1], self.minHeap[0]
            self.maxHeap.append(self.minHeap.pop())
            self.swimMax(self.maxHeap, len(self.maxHeap) - 1)
            
            if self.minHeap:
                self.sinkMin(self.minHeap, len(self.minHeap), 0)

    def findMedian(self) -> float:
        if len(self.minHeap) < len(self.maxHeap):
            return float(self.maxHeap[0])
        else:
            return (self.maxHeap[0] + self.minHeap[0]) / 2.0