class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        list2 = [ord(i) for i in s2]
        sum2 = sum(list2)
        list1 = [ord(i) for i in s1]
        target = sum(list1)
        if sum2 == target:
                return sorted(s1) == sorted(s2)
        left = 0
        sum_window = 0
        for right in range(len(list2)):
            sum_window += list2[right]
            while sum_window > target:
                sum_window -= list2[left]
                left += 1
            if sum_window == target and (sorted(s1) == sorted(s2[left:right+1])):
                return True
        return False