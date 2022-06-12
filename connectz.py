"""
    application:    connectz solver
    version:        1.0.0
    developer:      Peter Goteh Yaanwa
    mobile:         07733814044
    email:          edwardpeter547@gmail.com
    Language:       python:3.6 
    Coding-Style:   PEP8 Standard/Specification.
"""


import sys, pathlib, enum


"""
Name: GAME_BOARD - (scope: global, type: constant:dict, default-value: "{}")
Description: python dictionary to hold the all player moves for each column"""   
GAME_BOARD = {}


"""
Name: GAME_DATA - (scope: global, type: constant:dict, default:{} )
Description: Dictionary type datastructure to hold the game configuration from the 
inputfile.txt the configuration includes the game_dimension data (X Y Z) from the
first line of the inputfile.txt and the players game moves data
"""
GAME_DATA = {}


"""
Name: GAME_BOARD_KEY - (scope: global, type: constant:str, default-value: "connectz")
Description: constant to hold the key to selecting the 2D array holding the moves
for both player one and player two.
"""
GAME_BOARD_KEY = "connectz"


"""
Name: FRAME_WIDTH_KEY - (scope: global, type: constant:str, default-value: "column")
Description: dictionary key constant to retrieve the (X) value representing the column 
from the dimension data read from the first line of the input file. this key is passed 
to the GAME_DATA Dictionary holding the three (3) Dimension data (X Y Z) to retrieve the
(X) value of the dimension data.
"""
FRAME_WIDTH_KEY = "column"


"""
Name: FRAME_HEIGHT_KEY - (scope: global, type: constant:str, default-value: "row")
Description: A dictionary key constant to retrieve the (Y) value representing the row 
from the dimension data read from the first line of the input file. this key is passed 
to the GAME_DATA Dictionary holding the three (3) Dimension data (X Y Z) to retrieve the
(Y) value of the dimension data.
"""
FRAME_HEIGHT_KEY = "row"


"""
Name: WIN_COUNTER_KEY - (scope: global, type: constant:str, default-value: "counter")
Description: A dictionary key constant to retrieve the (Z) value representing the 
total required wining combination of moves, specified as (Z) from the first line of 
the inputfile.
"""
WIN_COUNTER_KEY = "counter"


"""
Name: PLAYER_ONE_MOVE_DATA - (scope: global, type: constant:int, default-value: 1 )
Description: An Integer type key constant used to represent the move data for 
player one moves. this can be retrieved to check for a winning condition from the 
GAME_BOARD 2D array of player one moves.
"""
PLAYER_ONE_MOVE_DATA = 1


"""
Name: PLAYER_TWO_MOVE_DATA - (scope: global, type: constant:int, default-value: 2 )
Description: An Integer type key constant used to represent the move data for 
player two moves. this can be retrieved to check for a winning condition from the 
GAME_BOARD 2D array of player two moves.
"""
PLAYER_TWO_MOVE_DATA = 2


"""
Name: EXPECTED_FILE_ARGS - (scope: global, type: constant:int, default-value: 2 )
Description: An Integer type key constant to check the total expected sys.argv 
by default sys.argv has a default argument of the program filename and an expected
additional parameter of inputfile for the game data total accepted argument 2.
"""
EXPECTED_SYS_ARGS = 2


class Output(enum.Enum):
    
    """
    Name: PLAYER_ONE_WIN - (scope: global, type: constant:int, default-value: 1 )
    Description: describes the output specification / value for player one win
    """
    PLAYER_ONE_WIN = 1


    """
    Name: PLAYER_TWO_WIN - (scope: global, type: constant:int, default-value: 2 )
    Description: describes the output specification / value for player two win
    """
    PLAYER_TWO_WIN = 2


    """
    Name: DRAW_CONDITION - (scope: global, type: constant:int, default-value: 0 )
    Description: describes the output specification / value for a draw condition.
    """
    DRAW_CONDITION = 0


    """
    Name: INCOMPLETE - (scope: global, type: constant:int, default-value: 3 )
    Description: Describes the output condition where the file conforms to the format and 
    contains only legal moves, but the game is neither won nor drawn by either player and 
    there are remaining available moves in the frame. Note that a file with only a dimensions
    line constitues an incomplete game.
    """
    INCOMPLETE = 3


    """
    Name: ILLEGAL_CONTINUE - (scope: global, type: constant:int, default-value: 4 )
    Description: Describes the output condition where All moves are valid in all other respects but 
    the game has already been won on a previous turn so continued play is considered an illegal move.
    """
    ILLEGAL_CONTINUE = 4


    """
    Name: ILLEGAL_ROW - (scope: global, type: constant:int, default-value: 5 )
    Description: Describes the output condition where The file conforms to the format and all moves 
    are for legal columns but the move is for a column that is already full due to previous moves.
    """
    ILLEGAL_ROW = 5


    """
    Name: ILLEGAL_COLUMN - (scope: global, type: constant:int, default-value: 6 )
    Description: Describes the output condition where The file conforms to the format but contains
    a move for a column that is out side the dimensions of the board. i.e. the column selected is 
    greater than X
    """
    ILLEGAL_COLUMN = 6


    """
    Name: ILLEGAL_GAME - (scope: global, type: constant:int, default-value: 7 )
    Description: Describes the output condition where The file conforms to the format but the
    dimensions describe a game that can never be won.
    """
    ILLEGAL_GAME = 7


    """
    Name: INVALID_FILE - (scope: global, type: constant:int, default-value: 8 )
    Description: Describes the output condition where The file is opened but does not conform 
    to the format.
    """
    INVALID_FILE = 8


    """
    Name: FILE_ERROR - (scope: global, type: constant:int, default-value: 9 )
    Description: Describes the output condition where The file can not be found, opened or read 
    for some reason.
    """
    FILE_ERROR = 9


    """
    Name: INVALID_FILE_ARGUMENT - 
    (scope: global, type: constant:str, default-value: connectz.py: Provide one input file )
    Description: Describes the output condition where If the game is run with no arguments or more 
    than one argument it should print the following message as a single line to standard out.
    """
    INVALID_FILE_ARGUMENT = f"{sys.argv[0]}: Provide one input file"


class DimensionData(enum.Enum):
    """
    Name: X - (scope: global, type: constant:int, default-value: 0 )
    Description: An Integer type key constant used to store/retrieve value for the (X)
    from a list holding dimension data in GAME_DATA Dictionary.
    """
    X = 0
    
    """
    Name: Y - (scope: global, type: constant:int, default-value: 1 )
    Description: An Integer type key constant used to store/retrieve value for the (Y)
    from a list holding dimension data in GAME_DATA Dictionary.
    """
    Y = 1
    
    """
    Name: Z - (scope: global, type: constant:int, default-value: 2 )
    Description: An Integer type key constant used to store/retrieve value for the (Z)
    from a list holding dimension data in GAME_DATA Dictionary.
    """
    Z = 2
    
    
class Result:
    
    @staticmethod
    def display_result(output_condition):
        """
        Displays output condition to the terminal and exits the program.
        Arguments:
            output_condition: a constant that represents the output condition of the program.
        """
        
        # prints the output condition of the program to the console.
        print(output_condition)
        
        
        # exits the program with exit function call.
        exit()
        
    
class ConnectZ:
    
    @classmethod
    def is_valid_location(cls,board, col):
        """
        this function checks if a valid move can be made on a specific column and returns
        true. or false if the column cannot accept any more moves.

        Args:
            board (list): board is a list of sublist for a MxN matrix corresponding to the 
            columns and row specification from the first line of the input file. it holds
            the positional moves for both player 1 and player two.
            col (int): this represents the column where the player wants to place the next
            move.

        Returns:
            bool: returns true if the position at specific column does not have the default
            value 0. this indicates that there is no move at that column or the column is 
            available to take one or more moves.
        """
        return board[GAME_DATA.get(FRAME_HEIGHT_KEY) - 1][col] == 0 #type: ignore
   
    
    @classmethod
    def set_move(cls, board, row, col, player_move_data):
        """
            set_move function places a players move at the next avialable row in the players
            selected column.
        Args:
            board ([[]]): board is a list of sublist for a MxN matrix that holds all
            positional moves for player 1 and player 2
            
            col (int): this represents the column where the player wants to place the next
            move.
            
            row (int): represents the row where the player move is placed within the 
            selected column.
            
            col (int): represents the column where the player places his/her next move.
            
            player_move_data (int): when a player makes his/her move for a specific [row][col] 
            the integer is placed in that position indicating a move for that player
        """
        board[row][col] = player_move_data
        

    @classmethod
    def get_next_position(cls, board, col):
        """
        This function returns the next available position (row) for a selected column.

        Args:
            board (list(list)): board is a list of sublist for a MxN matrix that holds all
            positional moves for player 1 and player 2
            col (int): this represents the column where the player wants to place the next
            move.

        Returns:
            int: indicates the next available row from a selected column where the player
            wants to place the next move data.
        """
        
        
        # get the total rows from the GAME_DATA data structure using the FRAME_HEIGHT_KEY constant. this indicates the rows data (Y)        
        total_rows = GAME_DATA.get(FRAME_HEIGHT_KEY) - 1 #type: ignore 
        
        # ilterate through all the rows in a specific column and return the next position without a players move data. 
        for row in range(total_rows + 1):
            if board[row][col] == 0:
                return row
            

    
    @classmethod
    def check_win_move(cls, board, row, col, player_move_data):
        """
            Checks if there was a win condition horizontally, vertically, forward-diagonally, backward-diagonally. and returns True else returns False
        Args:
            board (list(list)): board is a list of sublist for a MxN matrix that holds all positional moves for player 1 and player 2
            row (int): this represents the row where he last move was placed for a particular player.
            col (int): this represents the column where the last move was placed for a particular player.
            player_move_data (int): the integer corresponding to a move data for a specific player. (1) for player 1 and (2) for player 2

        Returns:
            bool: Returns True if there was a win based on the last move, for a specific row and column for that player.
        """
        
        # returns all horizontal moves from the moves list MxN matrix
        horizontal_moves = board[row]
        
        
        # returns all vertical moves from the moves list MxN matrix
        vertical_moves = [board[i][col] for i in range(len(board))]
        
        
        # Flag to check boolean value for diagonal win. default: False
        is_diagonal_win = False
        
        
        # Check if there was a horizontal win and return True
        if cls.verify_win(horizontal_moves, player_move_data):
            return True
        
        
        # Check if there was a vertical win and return True
        if cls.verify_win(vertical_moves, player_move_data):
            return True
        
        
        # returns list of forward-diagonal moves and backward-diagonal moves from the moves list MxN matrix
        diagonal_moves = cls.get_diagonal_elements(board)
        
        
        # Ilterate through the sublist of forward-diagonal and backward-diagonal moves and return True if there was a win from previous move.
        for i in range(len(diagonal_moves)):
            if cls.verify_win(diagonal_moves[i], player_move_data):
                is_diagonal_win = True
                break
        
        # Checks if the Flag was set (True) for any forward-diagonal / backward-diagonal win and return True.
        if is_diagonal_win == True:
            return True
        
        # Returns False if no win condition was found based on the last user move.
        return False
    
    
    @classmethod
    def verify_win(cls, linear_moves, player_move_data):
        """
        This function verifies if there was a win from the last move. it takes as arguments list of linear moves and players specific move to check if there was a win for that player.
        Args:
            linear_moves (list): list of linear moves (horizontal moves, vertical moves, forward-diagonal/backward-diagonal moves) from the MxN matrix of players moves.
            player_move_data (int): the integer corresponding to a move data for a specific player. (1) for player 1 and (2) for player 2

        Returns:
            bool: Returns True if there was a win condition. and False if there was no win condition for a specific player.
        """

        # Initial flag to count the columns. Initial value is 0
        counter = 0
        
        
        # gets the total required moves to get a win condition from the GAME_DATA data structure with the WIN_COUNTER_KEY string constant.
        win_counter = GAME_DATA.get(WIN_COUNTER_KEY)
        
        
        # Initialize a List to hold the boolean values indicating consistent consecutive linear win conditions. 
        consecutive_linear_moves = []
        
        
        # Ilterate through the list of linear moves 
        while counter < len(linear_moves):
            
            
            # Check and break the loop if the total consecutive linear moves list equals the required total moves for a win condition indicated by (Z) from the input file.
            if len(consecutive_linear_moves)  == win_counter:
                break
            
            
            # append a True in the list of consecutive move data for current player if the move at counter position is equal to the current players move data. else remove all existing values.
            if linear_moves[counter] == player_move_data:
                consecutive_linear_moves.append(True)
            else:
                consecutive_linear_moves.clear()
                
            
            # increment the loop control flag counter to the next position on the linear list of moves.
            counter += 1
            
        
        # set return value of the function to True if we already have the required total consecutive moves for a win condition. else return False
        if len(consecutive_linear_moves) == win_counter:
            return True
        else:
            return False
    
    
    @classmethod 
    def get_diagonal_elements(cls, board):
        """
        This function returns a list containing a sublist of all forward-diagonal and backward diagonal elements from the MxN Matrix for all moves.
        Args:
            board (list(list)): board is a list of sublist for a MxN matrix that holds all positional moves for player 1 and player 2

        Returns:
            list(list): returns a list containing a sublist of forward-diagonal and backward diagonal elements from the MxN Matrix
        """
        
        # get total winning moves (Z) as specified in the dimension data of the input file stored in the GAME_DATA data structure. this is retireved using the WIN_COUNTER_KEY string constant
        required_winning_moves = GAME_DATA.get(WIN_COUNTER_KEY)
        
        
        # get the length of the column (total number of columns. this value is denoted as X in the input file)
        max_col = len(board[0])
        
        
        # get the height of the rows (total number of rows. this value is denoted as Y in the input file)
        max_row = len(board)
        
        
        # initialize a sublist for all the possible forward diagonals from the MxN matrix.
        forward_diagonals = [[] for _ in range(max_row + max_col - 1)]
        
        
        # initialize a sublist for all the possible backward diagonals from the MxN matrix.
        backward_diagonals = [[] for _ in range(len(forward_diagonals))]
        
        
        # get the mininum backward diagonals
        min_backward_diagonals = -max_row + 1
        
        
        # while ilterating through the max row and column append elements at position [y][x] of the MxN matrix to the summation of forward_diagonals[x+y] and backward_diagonals[x-y-min_backward_diagonals]
        for x in range(max_col):
            for y in range(max_row):
                forward_diagonals[x+y].append(board[y][x])
                backward_diagonals[x-y-min_backward_diagonals].append(board[y][x])
        
        
        # join both backward diagonal sublist to forward diagonal list to make a single list of all possible diagonals.
        forward_diagonals.extend(backward_diagonals)
        
        
        # using list comprehension filter the list of forward diagonals and backward diagonals for sublist with items with the same length as to total required winning moves (Z) as specified in the input file.
        all_diagonals = [x for x in forward_diagonals if len(x) >= int(required_winning_moves)]
        
        
        # remove repeated diagonal sublist items using a set which takes a map function with a tuple and all diagonals as parameter
        filtered = [list(i) for i in set(map(tuple, all_diagonals))]
        
        
        # return the filtered list which contains only unique diagonals sublist for forward and backward diagonal items greater than or equal to the required winning moves (Z)
        return filtered    
            
        
    @classmethod
    def set_game_board(cls, column_width, row_height):
        """
        This function sets the Data Structure for the game board to hold the MxN matrix for players moves. this method uses
        list comprehension to initialize the MxN matrix with 0's to form a sparse matrix.

        Args:
            column_width (int): Denotes the column as specified in the input file (X)
            row_height (int): Denotes the row as specified in the input file (Y)
        """
        GAME_BOARD.update({GAME_BOARD_KEY:[[0 for i in range(column_width)] for j in range(row_height)]})
    
    
    
    @classmethod
    def analyze(cls, board, selected_column, player_total_moves, required_winning_move, all_moves, counter, player_move_data, win_status_code):
        """
        This method analyzes the sets the players moves in their respective positions in the MxN matrix. calls the is_valid_location checker
        to asertain which column has not been filled, calls the set_move method on the row returned from the is_valid_location method.
        checks if the player has made enough move to complete a winning move. calls check_win_move method on the current move to check if the
        current player move is a winning move. calls display_result from the Result class if there is a Illegal Continue Condition after a 
        winning move.

        Args:
            board (list(list)): list with a sublist (2D array) of MxN matrix holding all player moves.
            selected_column (int): The players selected column for the current move.
            player_total_moves (int): Total moves for the current player.
            required_winning_move (int): Total required move to get a win condition.
            all_moves (int): Total moves from the game dataset.
            counter (int): _description_
            player_move_data (int): current player's move data. Default values (player one: 1, player two: 2)
            win_status_code (Enum): status code to pass to display_result method of Result class.
        """
        
        
        # Check if selected column is valid and not full for the player's current move.
        if cls.is_valid_location(board, selected_column):
            
            
                    # get the next available row/position on the player's selected column.
                    row = cls.get_next_position(board, selected_column)
                    
                    
                    # place the players move data (default values player one: 1, player two: 2) in the selected row and column.
                    cls.set_move(board,row, selected_column, player_move_data)
                    
                    
                    # ! Optimised Check: before checking for a winning move if the current player has made enough move to reach a win condition.
                    if player_total_moves >= required_winning_move:
                        
                        
                        # check if the users current move denotes a winning move for the specified row and column selected.
                        if cls.check_win_move(board, row, selected_column, player_move_data):
                            
                            
                            # if there was a win condition on the current move. check if there are still available moves that denotes an illegal continue condition.
                            if counter < all_moves:
                                Result.display_result(Output.ILLEGAL_CONTINUE.value)
                                
                            # if there was no extra moves to indicate an illegal continue. call dispaly_result method on Result class for the current user as winner.
                            Result.display_result(win_status_code.value)
        else:
            
            # if the selected column indicates a column that is already full as a result of the previous move. this indicates an Illegal Row.
            Result.display_result(Output.ILLEGAL_ROW.value)


class Utility:
    
    @classmethod
    def check_constraints(cls, selected_column, all_moves):
        """
        check_contraints method checks for a list for validation criteria to ensure that the players current move is valid.

        Args:
            selected_column (int): describes the players selected column for the current move.
            all_moves (int): denotes the total moves for both player 1 and player 2
        """
        if cls.is_incomplete(all_moves):
            Result.display_result(Output.INCOMPLETE.value)
        
        
        # checks if there is an illegal column condition.
        if cls.is_illegal_column(selected_column, GAME_DATA[FRAME_WIDTH_KEY]):
            Result.display_result(Output.ILLEGAL_COLUMN.value)
        
        
        # checks if there is an illegal row condition.
        if cls.is_illegal_row(selected_column, GAME_DATA[FRAME_HEIGHT_KEY]):
            Result.display_result(Output.ILLEGAL_ROW.value)
    
    
    @staticmethod
    def is_invalid_file(dimension):
        """
        The method checks if there is an format or negative values in the dimension values.

        Args:
            dimension (list): denotes the dimension from the input file for (X, Y, Z) values respectively. 
        """
        
        # if the length of the dimension is not equal to 3 denotes an invalid file .
        if len(dimension) != 3:
            Result.display_result(Output.INVALID_FILE.value)
        
        
        # check if the dimension data contains any negative value which denotes an Invalid File
        if any([x < 0 for x in dimension]):
            Result.display_result(Output.INVALID_FILE.value)
    
    
    @classmethod
    def is_illegal_game(cls, column_width, required_winning_moves):
        """
        This function checks if there is an illegal game condition.

        Args:
            column_width (int): total number of columns denoted by X from the input file
            win_counter (int): total number of consecutive moves required for a win condition.

        Returns:
            bool: returns False if the total required winning moves (win_counter) is less than Total Columns otherwise denotes an Illegal game.
        """
        
        
        # check if total required_winning_moves moves denoted by (Z) in the input file is greater than the total columns denoting an illegal game condition 
        if required_winning_moves > column_width:
            
            
            # Returns an Illegal Game constant to display_result method of Result class.
            Result.display_result(Output.ILLEGAL_GAME.value)
            
            
        # returns false if the total required moves denoted (Z) in the input file is less that the total columns.
        return False
    
    
    @classmethod
    def is_illegal_column(cls, selected_column_move, total_columns):
        """
        This function checks if there is an illegal column condition.

        Args:
            selected_column_move (int): Integer denoting the move for a selected column.
            total_columns (int): total number of columns denoted by X from the input file

        Returns:
            bool: Returns True if selected column move is greater than the total columns 
        """
        
        # returns a boolean value True if the selected column move is greater than the total available columns denoting an illegal column condition.
        return selected_column_move > total_columns
    
    
    
    @classmethod
    def is_illegal_row(cls, selected_column_move, total_rows):
        """
        This method checks and returns a boolean value if the selected column is already full and cannot accept any other move.

        Args:
            selected_column_move (int): denotes the move for a particular column
            total_rows (int): denotes the total number of rows (Y) from the input file.

        Returns:
            bool: returns a boolean flag if the selected column does not have any available row. denoting an illegal row condition.
        """

        return selected_column_move > total_rows
        
    
    
    @classmethod
    def is_incomplete(cls, total_moves):
        """
        This method checks if the data set contains incomplete moves. this method checks if the input file only contains the dimension data from the first line of the file.
        Args:
            total_moves (int): denotes the count() for all moves from the input file for both player 1 and player 2

        Returns:
            bool: returns a boolean flag if the length of moves is 0
        """
        
        
        return total_moves <= 0 
 
 
class GameData:
    
    @classmethod
    def set_game_data(cls, total_columns, total_rows, required_winning_move):
        """
        This method sets the game dimension data read from the first line of the input file in the GAME_DATA dictionary object.

        Args:
            total_columns (int): positive integer value denoting the column width (X)
            total_rows (int): positive integer value denoting the row height (Y)
            required_winning_move (int): positive integer denoting the total required move for a win condition (Z)
        """
        
        # check if there is no illegal game condition before updating the game data, data structure.
        if not Utility.is_illegal_game(total_columns, required_winning_move):
            GAME_DATA.update({FRAME_WIDTH_KEY:total_columns, FRAME_HEIGHT_KEY: total_rows, WIN_COUNTER_KEY: required_winning_move})
            

class ReadFile:
       
    @classmethod
    def get_filename(cls):
        """
        This method returns the filename passed as command line argument to the program.

        Returns:
            str: retrieves the string representing the filename from an ascii file passed through the command line as argument to the program.
        """
        
        # returns the first parameter passed as commandline argument to the program.
        return sys.argv[1]
    
    
    @classmethod
    def get_content(cls, filename):
        """
        This function reads the content of the file line by line and calls the Connectz.analyze method on each of the moves read from the file.
        the function does not store the data from the file in memory rather the moves is processed and analysed as the file handle 
        ilterates through the file.

        Args:
            filename (file): accepts a filename parameter and reads the content of the file line by line.
        """
        
        
        # gets the path to the filename and returns a file path object.
        file_path = pathlib.Path(filename)
        
        
        try:
            
            # using context manager to handle the file operation so we don't have to explictly close the file.
            with file_path.open(mode="r") as file: 
                
                
                # read the dimension data from the first line of the using using list comprehension. the dimension data is stored in a list object.
                dimension = [int(line) for line in file.readline().strip().split(" ")]
                
                
                # uses the is_valid_file method of the utility class to check if the data read from the first line is of valid format.
                Utility.is_invalid_file(dimension)
                
                
                # set the data structure to hold the dimension data from the first line of the file. i.e (X, Y, Z) data point values.
                GameData.set_game_data(dimension[DimensionData.X.value], dimension[DimensionData.Y.value], dimension[DimensionData.Z.value])
                
                
                # set the value for the column (X) from the game dimension Dictionary using the FRAME_WIDTH_KEY string constant
                column = GAME_DATA.get(FRAME_WIDTH_KEY)
                
                
                # set the value for the row (Y) from the game dimension Dictionary using the FRAME_HEIGHT_KEY string constant 
                row = GAME_DATA.get(FRAME_HEIGHT_KEY)
                
                
                # set the dimension of the game board MxN matrix 
                ConnectZ.set_game_board(column, row)
                
                
                # sets the local variable to hold the MxN matrix for the game board.
                board = GAME_BOARD.get(GAME_BOARD_KEY)
                
                
                # initialize/set flag for incomplete game condition with initial value of False.
                is_incomplete_game = False
                
                
                # define / initialize player 1 total move counter to 0
                player_one_total_moves = 0
                
                
                # define / initialize player 2 total move counter to 0
                player_two_total_moves = 0
                
                
                # sets the total required consecutive move for win condition (Z) from GAME_DATA dictionary using WIN_COUNTER_KEY string constant
                win_counter = int(GAME_DATA.get(WIN_COUNTER_KEY))

                
                # reset the file handle/pointer to the beginning of the file after reading the dimension data from the first line.
                file.seek(0)
                
                
                try:
                    
                    
                    # move the file pointer to the next line to count the total moves without adding the first line containing the dimension data.
                    next(file)
                    
                    
                    # count the total number of moves from the input file without reading the file into memory
                    total_lines = len(file.readlines())
                    
                    
                    # initialize loop control variable to alternate reading the moves from player one to player two and vice versa
                    count = 1
                    
                    
                    # reset file handle/pointer after counting the total numer of lines to first position.
                    file.seek(0)
                    
                    
                    # move the file pointer to the next line to start reading the first line of the players moves data.
                    next(file)
                    
                    
                    # boolean flag to check if any of the lines are empty. the default is False.
                    has_empty_line = False
                    
                    
                    # initialize next line counter.
                    next_line = 0
                    
                    
                    # main loop: while count <= total number of lines 
                    while count <= total_lines:
                        
                        
                        # checks flag if file has an empty line and moves the file handle/pointer to the last point in the file.
                        if has_empty_line:
                            file.seek(next_line)
                        
                        
                        # condition to assign and alternate the lines for player one. (if count % 2 ! == 0 then the move belongs to player one)
                        if count % 2 != 0:
                            
                            
                            # using list comprehension read single line from the file. 
                            data = [int(line) for line in file.readline().strip() if line]
                            
                            
                            # check if the data returned from the line is empty. reset the file handle set has_empty_line flag to True. return control to the beginnig of the ilterator.
                            if len(data) == 0:
                                has_empty_line = True
                                file.tell()
                                continue
                            
                            
                            # store the first data indicating the column move for player one.
                            player_one_move = data[0]
                            
                            
                            # check pass player one move data and total lines through some constraint checks if they are valid.
                            Utility.check_constraints(player_one_move, total_lines)
                            
                            
                            # reset player ones move data indicating the columns to use arrays 0th based indexing. so every column is reduced by 1 as the first column is 0th indexed.
                            player_one_move -= 1
                            
                            
                            # increment the total move specific to player one.
                            player_one_total_moves += 1
                            
                            
                            # analyze game moves to determine all game conditions for player 1.
                            ConnectZ.analyze(board, player_one_move, player_one_total_moves, win_counter, total_lines, count, PLAYER_ONE_MOVE_DATA, Output.PLAYER_ONE_WIN)
                        
                        
                       
                        else:
                             
                             
                             # using list comprehension read single line from the file.   
                            data = [int(line) for line in file.readline().strip() if line]
                            
                            
                            
                            # check if the data returned from the line is empty. reset the file handle set has_empty_line flag to True. return control to the beginnig of the ilterator.
                            if len(data) == 0:
                                has_empty_line = True
                                print(file.tell())
                                exit()
                                continue
                            
                            
                            
                            # store the first data indicating the column move for player two.
                            player_two_move = data[0]
                            
                            
                            
                            # check pass player two move data and total lines through some constraint checks if they are valid.
                            Utility.check_constraints(player_two_move, total_lines)
                            
                            
                            
                            # increment the total move specific to player two.
                            player_two_move -= 1
                            
                            
                            
                            # increment player two total moves
                            player_two_total_moves += 1
                            
                            
                            
                            # analyze game moves to determine all game conditions for player 2
                            ConnectZ.analyze(board, player_two_move, player_two_total_moves, win_counter, total_lines, count, PLAYER_TWO_MOVE_DATA, Output.PLAYER_TWO_WIN)
                            
                        
                        # increment loop control variable.
                        count += 1
                    
                    
                    
                    # Todo: check if the game is incomplete.
                    for row in range(len(board[0])): #type: ignore
                        for col in range(len(board)):
                            if board[row][col] == 0: #type: ignore
                                is_incomplete_game = True
                                break
                    
                    
                    
                    # Todo; Check for Draw Condition
                    if is_incomplete_game == True:
                        
                        # indicates incompete game condition
                        Result.display_result(Output.INCOMPLETE.value)
                        
                        
                    else:
                        
                        # indicates a draw condition for both players.
                        Result.display_result(Output.DRAW_CONDITION.value)
                
                
                # if there is a value error exception; indicates a Invalid File Error. this means the file was read but the format was invalid.
                except ValueError:
                    Result.display_result(Output.INVALID_FILE.value)
           
                
        # if there is a value error exception; indicates a Invalid File Error. this means the file was read but the format was invalid.       
        except ValueError:
            Result.display_result(Output.INVALID_FILE.value)
        
        
        # if there is an OSError exception raised; indicates a File Error. this means the file was not found or could not be read.
        except OSError:
            Result.display_result(Output.FILE_ERROR.value)
        
                     

def main():
    
    
    # checks to see if number of commandline arguments is greater than the expected commandline argument and sends an InvalidFileArgument Constant to the display_result of Result Class.
    if len(sys.argv) < EXPECTED_SYS_ARGS or len(sys.argv) > EXPECTED_SYS_ARGS:
        Result.display_result(Output.INVALID_FILE_ARGUMENT.value)
    
    

    # Read Inputfile content using the get_content method from the ReadFile class.
    ReadFile.get_content(ReadFile.get_filename())
    
    
   
""" PROGRAM ENTRY POINT"""  
if __name__ == "__main__":
    main()
    