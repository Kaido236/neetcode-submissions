class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                pop_index = stack.pop()
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                height = heights[pop_index]
                area = width*height
                largest = max(largest,area)
            stack.append(i)
        return largest
