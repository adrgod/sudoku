# To build a sudoku game, we need to build the board, a 9x9 square.
# Initialize it means to fill in numbers in squares where: 
# row, columns and its 9 3x3 squares have only one number of each integer 1..9
# how to do that? My idea is to fill in number by number. starting on 1, filling all 1s to match the rows/cols rule
# and move on to next numbers, up to 9.


from sudoku_board import *

size = 3

def start():
    sdk = sudoku_board()
    sdk._initialize_board(size)
    sdk.fill_in_area(size)
    sdk.list_board()
    #sdk.print_board(size)
    #sdk.test_board()


if __name__ == '__main__':
    start()

