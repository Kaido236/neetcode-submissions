import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sum_piles = sum(piles)
        dis = math.ceil(sum_piles/h)
        ms = max(piles)
        left = dis
        right = ms
        h_temp_left = sum([math.ceil(i/dis) for i in piles])
        if h_temp_left == h:
            return dis
        h_temp_right = sum([math.ceil(i/ms) for i in piles])
        result = 0
        if h_temp_right == h:
            result = ms
        while left < right:
            mid = (left + right)//2
            h_temp = 0
            for i in piles:
                h_temp += math.ceil(i/mid)
            if h_temp > h:
                left = mid + 1
            elif h_temp < h:
                right = mid 
            elif h_temp == h:
                result = mid
                right = mid
        if left == right:
            return left
        return result