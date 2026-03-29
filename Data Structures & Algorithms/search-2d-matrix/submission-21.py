class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search throught the cols matrix
        # search on the row
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m-1
        while start < end:
            mid = (start+end) // 2
            if matrix[mid][-1] > target:
                end = mid
            elif matrix[mid][-1] < target:
                start = mid + 1
            else:
                break

        # When the end >= start we found the row
        pos = (start+end)//2
        print('ola', pos)
        row = matrix[pos]
        start = 0
        end = n - 1
        while start <= end:
            mid = (start+end) // 2
            if matrix[pos][mid] < target:
                start = mid + 1
            elif matrix[pos][mid] > target:
                end = mid - 1 
            else:
                return True

        return False



