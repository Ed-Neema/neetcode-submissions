class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while r>=l:
            mid = (l+r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                return self.binary_search(matrix[mid], target)
                 
        return False
        
    def binary_search(self, arr, target):
        l, r = 0, len(arr) - 1
        while r>=l:
            mid = (l+r) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
