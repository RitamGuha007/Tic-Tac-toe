import math
#Displaying the board
def print_board(board):
        for row in board:
            print(" | ".join(row))
        print()
# Check for a winner
def check_winner(board):
    #Rows
    for row in board:
        if row.count(row[0])==3 and row[0]!=' ':
            return row[0]
    #columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    #diagonals
    if board[0][0]==board[1][1]==board[2][2]!=' ':
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0]!=' ':
        return board[0][2]
    return None
    
#check if any moves left
def moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# minimax Algorithm
def minimax(board,depth,is_maximizing,alpha,beta):
    winner=check_winner(board)
    if winner=='O':
        return 1
    elif winner=='X':
        return -1
    elif not moves_left(board):
        return 0

    if is_maximizing:
        best_score=-math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]==' ':
                    board[i][j]='O'    
                    score = minimax(board,depth+1,False,alpha,beta)
                    board[i][j]=' '
                    best_score = max(score,best_score)
                    alpha=max(alpha,score)  
                    if beta<=alpha:
                       break
        return best_score
    else:
        best_score=math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j]==' ':
                    board[i][j]='X'
                    score=minimax(board,depth+1,True,alpha,beta)
                    board[i][j]=' '
                    best_score=min(score,best_score)
                    beta=min(beta,score)
                    if beta<=alpha:
                        break
        return best_score

# AI move
def best_move(board):
    best_score=-math.inf
    move=None
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
               board[i][j]='O'
               score=minimax(board,0,False,-math.inf,math.inf)
               board[i][j]=' '
               if score>best_score:
                  best_score=score
                  move=(i,j)
    return move 

# Main game loop 
def play_game():
    board=[[' ' for _ in range(3)]for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X-AI is O")
    print_board(board)
    while True:
        # Human Turn
        while True:
            try:
                row=int(input("Enter Row (0-2):"))
                column=int(input("Enter Column(0-2):"))
                if board[row][column]==' ':
                    board[row][column]='X'
                    break
                else:
                    print("Cell already Taken! Try Again.")
            except(ValueError,IndexError):
                print("Invalid Input! Enter numbers in range 0-2.")
        print_board(board)
        if check_winner(board)=='X':
            print("You Win! Congrats.")
            break
        if not moves_left(board):
            print("Its a Draw!")
            break
        
        # AI Turn
        print("AI is making a move....")
        row,col=best_move(board)
        board[row][col]='O'
        print_board(board)

        if check_winner(board)=='O':
            print("AI Wins! Guess U are a Loser.")
            break
        if not moves_left(board):
            print("Its a Draw!")
            break

if __name__=="__main__":
    play_game() 
    
