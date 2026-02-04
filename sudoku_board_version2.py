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
        try:
            for row in range(len(self.board[0])):
                col.append(self.board[row][pos])
            return col
        except:
            print(f"Column {pos} doesn't exist!") 
        
    
    def _get_row(self, row_number):
        try:
            return self.board[row_number]
        except:
             print(f"Row {row_number} doesn't exist!")
    
    def insert_element(self, value, row, col):
        try:
            self.board[row][col] = value
        except:
            print(f"Error inserting {value} in cell: ({row},{col})!")
    
    def elem_that_fits(self, values, row, col, row_to_insert, col_to_insert):
        result = []
        for value in values:
            if(
                self.board[row][col] == 0 and
                value not in row_to_insert and
                value not in col_to_insert
            ):
                result.append(value)
        
        return result
                
    
    def insert_missing(self, size, row, col):
        elems_in_row = set(self._get_row(row))
        elems_in_col = set(self._get_column(col))

        values = set(range(1, size + 1))

        print(f"elems in row: {elems_in_row}")
        print(f"elems in col: {elems_in_col}")

        missing_value = values - (elems_in_row & elems_in_col) - {0}

        self.insert_element(missing_value.pop(),row, col)


    def fill_in_area(self, size):
        
        next_elem_fits = False
        rows = list(range(size))
        columns = list(range(size))
        not_inserted = {}

        for row in rows:
            for column in columns:
                if self.board[row][column-1] == 0:
                    pass
                values = list(range(1, size + 1)) # a list to shuffle and pop each unique numbers to fill in
                shuffle(values)
                while values:
                    value = values.pop()
                    row_to_insert = self._get_row(row)
                    col_to_insert = self._get_column(column)
                    if column == size-2 and len(values) == 2:
                        try:
                            next_col = column+1
                            next_col_to_insert = self._get_column(next_col)
                            next_elem_that_fits = self.elem_that_fits(values,row, next_col, row_to_insert, next_col_to_insert)
                            if not next_elem_that_fits:
                                if(
                                    self.board[row][next_col] == 0 and
                                    value not in row_to_insert and
                                    value not in next_col_to_insert
                                ):
                                    self.insert_element(value, row, next_col)
                                    if(
                                        self.board[row][column] == 0 and
                                        not values or
                                        (values[0] not in row_to_insert and
                                        values[0] not in col_to_insert)
                                    ):
                                        self.insert_element(values[0], row, column)
                        except:
                            pass
                    if(
                        self.board[row][column] == 0 and
                        value not in row_to_insert and
                        value not in col_to_insert
                    ):
                        self.insert_element(value, row, column)
                        break
                    elif column == size - 1 and value not in self.board[row]:
                        not_inserted[value] = [row, column] # this means we reached the end of the line and didn't insert the value. But value needs to be inserted in the row so we append it back to rey again later
        
        print(f"Didnt' insert: {not_inserted.items()}.")

        for elem in not_inserted: 
             self.insert_missing(size, not_inserted[elem][0], not_inserted[elem][1])
             
             
               


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
