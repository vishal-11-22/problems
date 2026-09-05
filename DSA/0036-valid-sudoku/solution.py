class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            r_set=set()
            for ele in i:
                if ele!='.':
                    if ele in r_set:
                        return False
                    else:
                        r_set.add(ele)
        for i in range(len(board)):
            c_set=set()
            for j in range(len(board)):
                ele=board[j][i]
                if ele!='.':
                    if ele in c_set:
                        return False
                    else:
                        c_set.add(ele)

        indices={
            0:[0,1,2],
            1:[3,4,5],
            2:[6,7,8],
        }
        for mr in indices.values():
            
            for mc in indices.values():
                grid_set=set()
                for r in mr:
                    for c in mc:
                        if board[r][c]!='.':
                            if  board[r][c] in grid_set:
                                return False
                            else:
                                grid_set.add(board[r][c]) 
        return True