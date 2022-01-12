# W02 Prove: Developer - Solo Code Submission
# Wrote Marcos Rafael Uc Samos

def main():

    currently_player = "X"
    status = "Playing"
    turn = 1
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    print("Let's go to play Tic-Tac-Toe")
    print()
    print("This is the board")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---") 
    print(" 7 | 8 | 9 ")  
    print("El el jugador X comienza:")
        
    while(True):
        
        print(f"it's the player's turn {currently_player}")
        position = int(input("Chose your position (1-9): ")) - 1
        if position>=0 or position<=9:
            
            if board[position] != " ":
                print(f"The position {position} already ocupped, please chose other")
                continue
            else:
                board[position] = currently_player
                turn = turn + 1
        else:
            print("Invalid position")
            continue
        
        draw_board(board)

        status = board_status(board,status)

        if status == "Playing":
 
            if currently_player == "X":
                currently_player = "O"
            else:
                currently_player = "X"
        else:
            print(f"The game has been won by the player {currently_player}")
            break
 
        if turn >= 9:
            print("There are no more squares available this is a Draw")
            break



def draw_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def board_status(board,status):
    #check the horizontal lines
    if board[0] == board[1] == board[2] != " ":
        status = "Winner"
    elif board[3] == board[4] == board[5] != " ":
        status = "Winner"
    elif board[6] == board[7] == board[8] != " ": 
        status = "Winner"
    #check the vertical lines
    elif board[0] == board[3] == board[6] != " ":
        status = "Winner"
    elif board[1] == board[4] == board[7] != " ":
        status = "Winner"
    elif board[2] == board[5] == board[6] != " ":
        status = "Winner"
    #check the diagonal lines
    elif board[0] == board[4] == board[8] != " ":
        status = "Winner"
    elif board[6] == board[4] == board[2] != " ":
        status = "Winner"
    else:
        status = "Playing"
    return status 



if __name__ == "__main__":
   main()