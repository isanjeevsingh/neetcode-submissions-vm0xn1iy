from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check row
        for row in board:
            counts = [x for x in row if x != "."]
            if len(counts) > 0:
                if max(Counter(counts).values()) > 1:
                    return False
        
        # check column
        for i in range(9):
            col = []
            for row in board:
                col.append(row[i])
            counts = [x for x in col if x != "."]
            if len(counts) > 0:
                if max(Counter(counts).values()) > 1:
                    return False


        # check blocks
        block = []
        for offset in [0,3,6]:
            for i in range(9):
                for j in range(offset, 3+offset):
                    #print(f"{i=} {j=}")
                    block.append(board[i][j]) 
                if i in [2,5,8]:
                    # print(f"---") 
                    # print(f"{block=}")
                    counts = [x for x in block if x != "."]
                    if len(counts) > 0:
                        if max(Counter(counts).values()) > 1:
                            return False

                    block = []  
        return True
        