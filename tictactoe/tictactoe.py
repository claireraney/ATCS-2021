import random


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        # self.board = [["X", "O", "X"], ["O", "O", "X"], ["-", "X", "-"]]
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

    def take_random_turn(self, player):
        valid = False
        while (valid == False):
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            valid = self.is_valid_move(r, c)
            if valid == True:
                self.place_player(player, r, c)
            else:
                print("Input again.")

    def minimax(self, player):
        opt_row = -1
        opt_col = -1
        if self.check_win("O") == True:
            return 10, None, None
        if self.check_tie() == True:
            return 0, None, None
        if self.check_win("X") == True:
            return -10, None, None
        if player == "O":
            best = -100
            for i in range(0,3):
                for j in range(0,3):
                    if self.is_valid_move(i, j) == True:
                        self.place_player("O", i, j)
                        score = self.minimax("X")[0]
                        self.place_player("-", i, j)
                        if best < score:
                            opt_row = i
                            opt_col = j
                            best = score
            return best, opt_row, opt_col
        if player == "X":
            worst = 10
            for i in range(0,3):
                for j in range(0,3):
                    if self.is_valid_move(i, j) == True:
                        self.place_player("X", i, j)
                        score = self.minimax("O")[0]
                        self.place_player("-", i, j)
                        if worst > score:
                            opt_row = i
                            opt_col = j
                            worst = score
            return worst, opt_row, opt_col


    def take_minimax_turn(self, player):
        score, row, col = self.minimax(player)
        self.place_player(player, row, col)

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        if player == "X":
            self.take_manual_turn(player)
        else:
            self.take_minimax_turn(player)

    def check_col_win(self, player):
        # TODO: Check col win:
            for j in range(0, 3):
                if (self.board[0][j] == self.board[1][j] and self.board[0][j] == self.board[2][j]) and self.board[0][j] == player:
                    return True
            return False


    def check_row_win(self, player):
        # TODO: Check row win
        for i in range(0, 3):
                if (self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]) and self.board[i][0] == player:
                    return True
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
            if self.check_win(player):
                print(player, " wins!")
                break
            elif self.check_tie():
                print("Tie!")
                break
            if player == "X":
                player = "O"
            else:
                player = "X"



