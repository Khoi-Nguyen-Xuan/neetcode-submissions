class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first=0
        last=len(matrix)-1 
        row = 0
        while(first<=last):
            middle=int((first+last)/2) 
            if (matrix[middle][0] > target):
                last = middle-1 
            elif (matrix[middle][len(matrix[0])-1] <target): 
                first = middle+1
            else:
                break 
        
        if not (first <= last):
            return False 

        row = (first+last) // 2
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


        

        

            
        