class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        len_row = len_col = len(board[0])
        set_storage = []
        for i in range(len_row):
            set_storage = []
            for j in range(len_col):
                if (board[i][j] not in set_storage) and (board[i][j].isalnum()):
                    set_storage.append(board[i][j])
                elif (board[i][j] in set_storage) and (board[i][j].isalnum()):
                    return False
        
        set_storage = []
        for i in range(len_col):
            set_storage = []  
            for j in range(len_row):
                if (board[j][i] not in set_storage) and (board[j][i].isalnum()):
                    set_storage.append(board[j][i])
                elif (board[j][i] in set_storage) and (board[j][i].isalnum()):
                    return False
        
        set_storage = []
        for i in range(0,3):
            for j in range(0,3):
                set_storage = []
                for k in range(i*3,(i+1)*3):
                    for p in range(j*3,(j+1)*3):
                        if (board[k][p] not in set_storage) and (board[k][p].isalnum()):
                            set_storage.append(board[k][p])
                        elif (board[k][p] in set_storage) and (board[k][p].isalnum()):
                            return False

        return True

        