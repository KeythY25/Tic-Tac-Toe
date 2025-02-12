import math

# Tic-Tac-Toe Board Representation
PLAYER = 'X'
AI = 'O'

# Check for terminal state (win or draw)
def evaluate(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return 10 if row[0] == AI else -10
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return 10 if board[0][col] == AI else -10
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return 10 if board[0][0] == AI else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return 10 if board[0][2] == AI else -10
    
    return 0

# Check if moves are left
def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# Minimax Algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score - depth if score == 10 else score + depth
    if not is_moves_left(board):
        return 0
    
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = AI
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = ' '
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = ' '
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

# AI's Best Move
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = AI
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    
    return best_move

# Display board
def print_board(board):
    for row in board:
        print('|'.join(row))
    print('\n')

# Game Loop
board = [[' ' for _ in range(3)] for _ in range(3)]

def play_game():
    while True:
        print_board(board)

        # Player move
        try:
            row, col = map(int, input("Enter your move (row and column 0-2): ").split())
        except ValueError:
            print("Invalid input! Enter two numbers between 0 and 2.")
            continue
        
        if row not in range(3) or col not in range(3) or board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        
        board[row][col] = PLAYER
        
        if evaluate(board) == -10:
            print_board(board)
            print("You win!")
            break
        
        if not is_moves_left(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = AI

        if evaluate(board) == 10:
            print_board(board)
            print("AI wins!")
            break
        
        if not is_moves_left(board):
            print_board(board)
            print("It's a draw!")
            break

play_game()
``