import numpy as np

#creates empty sudoku board
board = np.zeros((9,9), dtype=np.int32) #for 2d arrays [row][col]
read_board_from_file("sodoku.in")

#function checks if the given row is valid
def _is_row_valid(row):
    assert row < 9 and row >= 0 , "row is out of range"
    count = np.zeros((9,), dtype = np.int32)
    for i in range(0,9):
        if board[row][i] == 0:
            continue
        elif (count[board[row][i] - 1]) >= 1:
            return False
        else:
            count[board[row][i] - 1] += 1
    return True

#function checks if the given column is valid
def _is_col_valid(col):
    assert col < 9 and col >= 0 , "column is out of range"
    count = np.zeros((9,), dtype = np.int32)
    for i in range(0,9):
        if board[i][col] == 0:
            continue
        elif (count[board[i][col] - 1]) >= 1:
            return False
        else: 
            count[board[i][col] - 1] += 1
    return True

#function checks if the given square is valid
def _is_square_valid(sqaure_row, sqaure_col):
    assert (sqaure_row < 3 or sqaure_col < 3) , "invalid square coordinates"
    row = sqaure_row * 3
    col = sqaure_col * 3
    count = np.zeros((9,), dtype = np.int32)
    for i in range(0,3):
        for j in range(0,3):
            if board[row + i][col + j] == 0:
                continue
            elif (count[board[row + i][col + j] - 1]) >= 1:
                return False
            else :
                count[board[row + i][col + j] - 1] += 1
    return True

#function checks if the entire board is valid
def _is_board_valid():
    for i in range(0,9):
        if (not _is_col_valid(i)) or (not _is_row_valid(i)):
            return False
    for i in range(0,3):
        for j in range(0,3):
            if (not _is_square_valid(i, j)):
                return False
    return True

#reads in a board from a file
#file should be in the format of 9 lines with 9 digits per line
def read_board_from_file(filename):
    infile = open(filename, "r")
    num_lines = 0
    for line in infile:
        if line == "\n" or line == "":
            continue
        line = "".join(line.split())
        assert (line.isdigit()), "none digit input in file: " + filename + "and line: " + str(num_lines+1)
        assert (len(line) == 9 or num_lines >= 9), "too many digits in file:" + filename + "\n"
        for i in range(0, 9):
            board[num_lines][i] = int(line[i])
        num_lines += 1

#writes board to a file
def write_board_to_file(filename):
    outfile = open(filename, "w")
    line = ""
    for i in range(0,9):
        for num in board[i]:
            line += str(num)
        line += "\n"
        outfile.write(line)
        line = ""
