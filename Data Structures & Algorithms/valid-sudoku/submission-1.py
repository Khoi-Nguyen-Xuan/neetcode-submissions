class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Check row 
        for row in board:
            if(self.isValidRow(row) == False): return False 
        
        #Check column
        cols = []
        for i in range(len(board)):
            col = []
            for j in range(len(board[0])):
                col.append(board[j][i])
            cols.append(col) 

        for col in cols:
            if(self.isValidRow(col) == False): return False 

        #Check box 
        boxs = []
        for i in range(0,len(board),3): 
            for j in range(0,len(board),3): 
                box = []
                box.append(board[i][j])
                box.append(board[i][j+1])
                box.append(board[i][j+2])
                box.append(board[i+1][j])
                box.append(board[i+1][j+1])
                box.append(board[i+1][j+2])
                box.append(board[i+2][j])
                box.append(board[i+2][j+1])
                box.append(board[i+2][j+2])
                boxs.append(box)

        for box in boxs:
            if(self.isValidRow(box) == False): return False 

        

        return True 


    def isValidRow(self, row: List[str]) -> bool: 
        my_dict = {}
        for num in row:
            if num != ".": 
                if num not in my_dict:
                    my_dict[num] = 0
                else: 
                    return False 
        
        return True 
        