import numpy as np

#read_board_from_file and write_board_to_file are functions for inputing and outputing
#sodoku puzzles from files.
#read_board_from_file reads a board from a file into memory, and write_board_to_file writes
#a sodoku puzzle to a file from memory

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

#_is_row_valid, _is_col_valid, and _is_square_valid checks if
#each aspect of the sodoku board (rows, column, and the 3x3 grid)
#do not have duplicate values in their squares, and _is_board_valid
#checks the entire board for validity

#function checks if the given row is valid
#takes in a row value 0-8, to check for validity
#returns true if all values in the row is unique and false otherwise
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
#takes in a column value 0-8 to check for validity
#returns true if column is valid, and false otherwise
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
#takes in a row and column, and checks the validity of the 3x3 square
#that coordinat falls in
#returns true if the 3x3 square is valid, false otherwise
def _is_square_valid(row, col):
    assert ((row < 9 and row >= 0) or (col < 9 and col >= 0)) , "invalid square coordinates"
    row = (row // 3) * 3
    col = (col // 3) * 3
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
            if (not _is_square_valid(i * 3 , j * 3)):
                return False
    return True


#creates empty sudoku board
board = np.zeros((9,9), dtype=np.int32) #for 2d arrays [row][col]
read_board_from_file("sodoku.in")
