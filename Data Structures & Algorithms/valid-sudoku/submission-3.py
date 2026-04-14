class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = set()
        cols = {i: set() for i in range(9)}
        squares = defaultdict(set)
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rowSet:
                    return False
                if board[i][j] in cols[j]:
                    return False
                if board[i][j] in squares[(i // 3, j // 3)]:
                    return False
                cols[j].add(board[i][j])
                rowSet.add(board[i][j])
                squares[(i // 3, j // 3)].add(board[i][j])
            rowSet.clear()

        return True
