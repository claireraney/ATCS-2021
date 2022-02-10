import random


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = []
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                row.append('-')
            self.board.append(row)


    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe!")
        print("Player 1 is X and Player 2 is O")
        print("Take turns putting your pieces down, and the first player to have 3 in a row wins!")

    def print_board(self):
        # TODO: Print the board
        print("\t0\t1\t2\t")
        for i in range(0, 3):
            print(i, "\t", end="")
            for j in range(0, 3):
                print(self.board[i][j] + "\t", end="")
            print("")



    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        # check to see if the input numbers are valid
        if (row > -1 and row <= 2) and (col > -1 and col <= 2):
            if self.board[row][col] == '-':
                return True
            else:
                return False
        else:
            return False


    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player


    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        valid = False
        while(valid == False):
            r = int(input("Please enter the row you want to place your piece at: "))
            c = int(input("Please enter the col you want to place your piece at: "))
            valid = self.is_valid_move(r, c)
            if valid == True:
                self.place_player(player, r, c)
            else:
                print("Input again.")


    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        self.take_manual_turn(player)

    def check_col_win(self, player):
        # TODO: Check col win
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.board[i][j] == self.board[i+1][j] and self.board[i][j] == self.board[i+2][j]) and self.board[i][j] == player:
                    return True
                else:
                    return False


    def check_row_win(self, player):
        # TODO: Check row win
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.board[i][j] == self.board[i][j+1] and self.board[i][j] == self.board[i][j+2]) and self.board[i][j] == player:
                    return True
                else:
                    return False
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        win1 = True
        win2 = True
        for i in range(0, 3):
            if self.board[i][i] != player:
                win1 = False
            if self.board[i][2-i] != player:
                win2 = False
        return win1 or win2

    def check_win(self, player):
        # TODO: Check win
        if self.check_row_win(player) == True or self.check_col_win(player) == True or self.check_diag_win(player) == True:
            print(player, " wins!")
            return True
        else:
            return False

    def check_tie(self):
        # TODO: Check tie
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == "-":
                    return False
        if self.check_win("X") == True or self.check_win("O") == True:
            return False
        else:
            return True


    def play_game(self):
        # TODO: Play game
        self.print_instructions()
        self.print_board()
        player = "X"
        while (True):
            self.take_turn(player)
            self.print_board()
            if self.check_win(player) or self.check_tie():
                break
            if player == "X":
                player = "O"
            else:
                player = "X"



