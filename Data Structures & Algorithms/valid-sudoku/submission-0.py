class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                box = (i//3)*3 + (j//3)
                val = board[i][j]
                if board[i][j]==".":
                    continue 
                
                if val in rows[i] or val in cols[j] or val in boxes[box]:
                    return False
                if val not in rows[i]:
                    rows[i].add(val)
                if val not in cols[j]:
                    cols[j].add(val)
                if val not in boxes[box]:
                    boxes[box].add(val)
                
        return True
                    


                

        
        
        