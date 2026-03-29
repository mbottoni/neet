class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_x = 0 
        start_y = 0

        end_x = len(matrix)-1
        end_y = len(matrix[0])-1

        while end_x >= start_x :
            mid_x = (start_x+end_x)//2
            if target < matrix[mid_x][0]:
                end_x = mid_x -1
            elif target > matrix[mid_x][len(matrix[0])-1]:
                start_x = mid_x +1
            else:
                # It is on this row
                while end_y >= start_y :
                    mid_y = (start_y+end_y)//2
                    if target < matrix[mid_x][mid_y]:
                        end_y = mid_y - 1
                    elif target > matrix[mid_x][mid_y]:
                        start_y = mid_y + 1
                    elif target == matrix[mid_x][mid_y]:
                        return True

                return False

        return False
        