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

    def _get_size(self):
        return len(self.board[0])
    
    def _get_next_column(self, size, column_number):
        if column_number < size - 1:
            return column_number + 1
        else:
            return column_number
    
    def insert_element(self, value, row_number, column_number):
        
        row_to_insert = self._get_row(row_number)
        col_to_insert = self._get_column(column_number)

        if(
            self.board[row_number][column_number] == 0 and
            value not in row_to_insert and
            value not in col_to_insert
        ):
            try:
                self.board[row_number][column_number] = value
                return 1
            except:
                print(f"Error inserting {value} in cell: ({row_number},{column_number})!")
                return -1
        else:
            return -1 # we need to know when the insert fails, so we can use if clause with function
    

    def elems_that_fit(self, values, row_number, column_number, row_to_insert, col_to_insert):
        result = []
        for value in values:
            if(
                self.board[row_number][column_number] == 0 and
                value not in row_to_insert and
                value not in col_to_insert
            ):
                result.append(value)
        
        return result
                
    def insert_missing(self):
        
        for row_number, row_data in enumerate(self.board):
            for column_number, column in enumerate(row_data):
                try:
                    if self.board[row_number][column_number] == 0:

                        column_data = set(self._get_column(column_number))

                        values = set(range(1, self._get_size() + 1))

                        print(f"elems in row: {row_data}")
                        print(f"elems in col: {column_data}")

                        missing_value = list(values - (set(row_data) | column_data))[0]

                        if missing_value:  # if there is a missing value
                            self.insert_element(missing_value, row_number, column_number)
                except Exception as e:
                    print(f"Error Inserting Missed Values, for value: {self.board[row_number][column_number]} in position: {(row_number, column_number)}")
                    print(type(e))


    def fill_in_area(self, size):
        
        rows = list(range(size))
        columns = list(range(size))
        
        not_inserted = {}

        for row in rows:
            for column_number in columns:
                if self.board[row][column_number-1] == 0:
                    pass
                values = list(range(1, size + 1)) # a list to shuffle and pop each unique numbers to fill in
                shuffle(values)
                while values:
                    value = values.pop()
                    row_to_insert = self._get_row(row)
                    col_to_insert = self._get_column(column_number)

                    next_column_number = self._get_next_column(len(self.board[0]), column_number) # return next column's data
                    next_column_data = self._get_column(next_column_number)
                    
                    # we can only insert a value in present location if we know there's a number that fits next position
                    # this next functions tells us if there's any value of the remaining values that fit next position.
                    next_elems_that_fit = self.elems_that_fit(values,row, next_column_number, row_to_insert, next_column_data)
                    
                    #now, until it's not the last column, we check if there's an elem left that can be inserted in next position
                    # if so, then we can run our tests to see if the present element can be inserted in present location
                    # if not, that means we need to swap elements: this present element needs to be insert in last position
                    # and next value in queue needs to be inserted in before-last position.
                    # so we avoid dead-ends, so tipycal in sudoku boards creations.
                    if column_number < size - 1: # while we're not looking at the last column...

                        if not(next_elems_that_fit): # if there's no next elem that fits last position
                            try:
                                self.insert_element(values[0], row, column_number) # we call insert function to try to insert next elem in before-last position
                                self.insert_element(value, row, next_column_number) # and we try as well to insert present elem in last position
                            except:
                                pass

                        else:
                            self.insert_element(value, row, column_number) # if there's elems that fit, we can insert present elem in present position, we know next elem will be inserted OK when his time comes.
                    else:
                        #if it's last elem/position to insert, try inserting last value
                        self.insert_element(value, row, column_number)

                    #if we missed to insert a value, we'll collect them now
                    #if column_number == size - 1 and value not in self.board[row]:
                    #    not_inserted[(row, column_number)] = value # this means we reached the end of the line and didn't insert the value. But value needs to be inserted in the row so we append it back to rey again later
        
        #print(f"Didnt' insert: {not_inserted.items()}.")

        # we go through the missed values and try to find the missing values to complete the board.
        for elem in self.board: 
            self.insert_missing()
             
             
               
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
