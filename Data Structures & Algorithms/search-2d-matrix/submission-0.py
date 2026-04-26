class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row by binary
        top, bot = 0, len(matrix) - 1
        rowMid = 0
        while top <= bot:
            mid = top + (bot - top) // 2
            if matrix[mid][0] <= target and matrix[mid][len(matrix[mid])-1] >= target:
                rowMid = mid
                break
            elif matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][0] < target:
                top = mid + 1
        
        l, r  = 0, len(matrix[rowMid])-1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[rowMid][mid] == target:
                return True
            elif matrix[rowMid][mid] < target:
                l = mid + 1
            elif matrix[rowMid][mid] > target:
                r = mid - 1
        return False