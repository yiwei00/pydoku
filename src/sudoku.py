import numpy as np

class sudoku:
    def __init__(self, k = 3, ):
        self._k = k
        self._n = k ** 2
        self._board = np.zeros((self.get_n(), self.get_n()), dtype=int)

    def get_n(self):
        return self._n

    def get_board(self):
        return self._board.tolist()

    def set_board(self, board):
        if not isinstance(board, list):
            return False
        if len(board) is not self._n:
            return False
        if not isinstance(board[0], list):
            return False
        if len(board[0]) is not self._n:
            return False
        if not isinstance(board[0][0], int):
            return False
        new_board = np.asarray_chkfinite(board, dtype=int)
        if not self.is_valid_board(new_board):
            return False
        self._board = new_board
        return True
    
    def is_valid_board(self, board=None):
        if not isinstance(board, np.ndarray):
            board = self._board
        for rows in board:
            count_arr = [0] * self._n
            for nums in rows:
                if nums == 0:
                    continue
                if count_arr[nums - 1] > 0:
                    return False
                else:
                    count_arr[nums - 1] = 1
        for cols in board.T:
            count_arr = [0] * self._n
            for nums in cols:
                if nums == 0:
                    continue
                if count_arr[nums - 1] > 0:
                    return False
                else:
                    count_arr[nums - 1] = 1
        for boxes in range(self._n):
            count_arr = [0] * self._n
            for i in range(self._n):
                r = self._k * (boxes // self._k) + (i // self._k)
                c = self._k * (boxes % self._k) + (i % self._k)
                print(f"Row: {r}, Col: {c}")
                num = board[r][c]
                if num == 0:
                    continue
                if count_arr[num - 1] > 0:
                    return False
                else:
                    count_arr[num - 1] = 1
        return True

game = sudoku(2)
my_board = [[1,2,3,4],[3,4,2,1],[2,1,4,3],[4,3,1,2]]
if game.set_board(my_board):
    print('yay')