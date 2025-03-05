def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return board[1][1]
    
    return None

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    
    for turn in range(9):
        print_board(board)
        player = players[turn % 2]
        print(f"{player}'s turn. Enter row and column (0-2):")
        
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter numbers between 0-2.")
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            return
    
    print_board(board)
    print("It's a tie!")

tic_tac_toe()
