board = {
    "1": " ", "2": " ", "3": " ",
    "4": " ", "5": " ", "6": " ",
    "7": " ", "8": " ", "9": " ",
}

def tic_tac_board():
    print(board["1"] + "  | " + board["2"] + " | " + board["3"])
    print("---+---+---")
    print(board["4"] + "  | " + board["5"] + " | " + board["6"])
    print("---+---+---")
    print(board["7"] + "  | " + board["8"] + " | " + board["9"])

def game():
    
    turn = "X"
    still_playing = True

    while still_playing:
        tic_tac_board()
        print(f"{turn} It's your turn, where do you want to go?")

        move = input()

        if board[move] == " ":
            board[move] = turn
        else:
            print("That spot is taken, please try again.")
            continue

        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        
        if (board["1"] == turn and board["2"] == turn and board["3"] == turn):
            print(f"Player {turn} Wins!")
            tic_tac_board()
            still_playing = False
        elif (board["1"] == turn and board["5"] == turn and board["9"] == turn):
            print(f"Player {turn} Wins!")
            tic_tac_board()
            still_playing = False
        elif (board["1"] == turn and board["4"] == turn and board["7"] == turn):
            print(f"Player {turn} Wins!")
            tic_tac_board()
            still_playing = False
        elif (board["2"] == turn and board["5"] == turn and board["8"] == turn):
            print("Player O Wins!")
            tic_tac_board()
            still_playing = False
        elif (board["3"] == turn and board["6"] == turn and board["9"] == turn):
            print(f"Player {turn} Wins!")
            tic_tac_board()
            still_playing = False
        elif (board["2"] == turn and board["5"] == turn and board["8"] == turn):
            print(f"Player {turn} Wins!")
            tic_tac_board()
            still_playing = False
        elif (board["3"] == turn and board["5"] == turn and board["7"] == turn):
            print(f"Player {turn} Wins!")
            tic_tac_board()
            still_playing = False
        else:
            continue




if __name__ == '__main__':
    game()
