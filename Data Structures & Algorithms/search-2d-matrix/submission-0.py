class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        max_row = [i[-1] for i in matrix]
        l = 0
        r = len(matrix)-1
        while l < r:
            mid = (l+r)//2
            if target < max_row[mid]:
                r = mid
            elif target > max_row[mid]:
                l = mid + 1
            else:
                return True
        arrays = matrix[l]
        l = 0
        r = len(arrays)-1
        while l < r:
            mid = (l+r)//2
            if target < arrays[mid]:
                r = mid
            elif target > arrays[mid]:
                l = mid + 1
            else:
                return True
        if l == r:
            if arrays[l] == target:
                return True
        return False
        