class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            if r[-1] < target:
                continue
            else:
                #binary search
                left = 0
                right = len(r) - 1
                while left <= right:
                    mid = (left+right) // 2
                    if r[mid] == target:
                        return True
                    elif r[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
        return False
