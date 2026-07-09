class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        if height == sorted(height) or height == sorted(height,reverse = True):
            return 0
        temp = 0
        overflow = 0
        dis = 0
        l,r = 0,len(height)-1
        while (height[l] < height[l+1]):
            l+=1
        while (height[r] < height[r-1]):
            r-=1
        waters = {i:0-height[i] for i in range(l,r+1)}
        while l<r:
            if height[l] < height[r]:
                dis = height[l]
                overflow = max(0,dis-temp)
                temp = max(dis,temp)
                if overflow != 0:
                    for i in range(l+1,r):
                        waters[i] += overflow
                l += 1
            if height[l] >= height[r]:
                dis = height[r]
                overflow = max(0,dis-temp)
                temp = max(dis,temp)
                if overflow != 0:
                    for i in range(l+1,r):
                        waters[i] += overflow
                r -= 1
        return sum(value for value in waters.values() if value > 0)
        