from random import randint, shuffle

class sudoku_board:

    def __init__(self):
        self.board = [] # the board itself
        self._coordinates = {} # dict to store numbers' coordinates
    
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
    
    def get_column_data(self, column):
        column_data = []

        for number in self._coordinates.keys():
                for position, element in enumerate(self._coordinates[number]):
                    if position == column: 
                        column_data.append(element)
        
        return column_data
    
    def number_fits_next_spot(self, size, value, key, column):
        elements = []

        for n in range(key+1, size+1):
            try:
                elements.append(self._coordinates[n][column])
            except:
                pass
        
        if value in elements:
            return False
        else:
            return True

    def create_positions(self, size, value):
        result = {}
        existing_coordinates = {}
        used_numbers = []

        for column in range(0, size):
            existing_coordinates = self.get_column_data(column)

            values_to_fill = list(set(range(1, size + 1)) - set(existing_coordinates) - set(used_numbers)) 

            #shuffle(values_to_fill)

            
            try:
                value_to_insert = values_to_fill[0]
            except:
                value_to_insert = -1
            
            if column == size-1:
                if not(self.number_fits_next_spot(size, value_to_insert, value, column+1)):
                    result.setdefault(value,[]).append(value_to_insert)
            
            used_numbers.append(value_to_insert)

        return result

                
    

    def fill_in_area(self, size):
        
        values = range(1,size+1)

        for number in values:
            self._coordinates.update(self.create_positions(size, number))

        print(self._coordinates)

             
             
               
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
