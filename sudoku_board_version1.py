from random import randint, shuffle

class sudoku_board:

    def __init__(self):
        self.board = [] # the board itself
        self._coords = {} # dict to store numbers' coordinates
    
    def _initialize_board(self, size):
        for i in range(size):
            temp = []
            for j in range(size):
                temp.append(0)
            self.board.append(temp)
        
    def _get_column(self, pos):
        col = []
        if self.board == [[]]:
            return []
        for row in range(len(self.board[0])):
            col.append(self.board[row][pos])
        return col
    
    def _get_row(self, row_number):
        return self.board[row_number]
    
    def _insert_number(self, num, row, pos):
        self.board[row][pos] = num
    

    def fill_in_area(self, size):
        values = list(range(1, size + 1)) # a list to shuffle and pop each unique numbers to fill in
        shuffle(values)
        while values:
            number_to_add = values.pop() # get value to insert
            
            n_rows = list(range(size))
            n_rows.reverse()
            while n_rows:
                row = n_rows.pop()
                insert_locs = list(range(size)) # unique list of locations number
                shuffle(insert_locs)
                while insert_locs:
                    pos = insert_locs.pop() # get location in row to insert number
                    column_to_check = self._get_column(pos)
                    row_to_check = self._get_row(row)
                    #if it's row before last, check if last row can hold last value (if position is not used already)
                    if len(n_rows) == len(insert_locs) == 1:
                        next_column_to_check = self._get_column(insert_locs[0])
                        next_row_to_check = self._get_row(n_rows[0])
                        if (
                                next_column_to_check[n_rows[0]] == 0 and number_to_add not in next_column_to_check and 
                                number_to_add not in next_row_to_check
                            ):
                                self._insert_number(number_to_add, row, pos)
                                break
                    if (
                            column_to_check[row] == 0 and number_to_add not in column_to_check and 
                            number_to_add not in row_to_check
                        ):
                        self._insert_number(number_to_add, row, pos)
                        break
                        


    def list_board(self):
        for rows in range(len(self.board)):
                for cols in range(len(self.board[0])):
                    print(f"Element in position ({rows}, {cols}): {self.board[rows][cols]}")

    def print_board(self, size):
        o = []

        o.append(" ".join("|"))
        for i in range(len(self.board[0])):
            o.append(" ".join("----"))
        o.append(f"| {self.board[0][0]}")
        for i in range(3):
            o.append(" ".join("----"))
        o.append(" ".join("|"))
        print(o)
            