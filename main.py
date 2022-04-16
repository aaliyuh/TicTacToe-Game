def initialize(n):
    board= []
    for r in range(n):
        board.append([])
        for c in range(n):
            board[r].append('.')
    return board

def show(board,n):
    for r in range(n):
        for c in range(n):
            print(board[r][c], end="")
        print("")
    board = initialize(n)
    board[1][1]="O"


def userinput(board,player):
    s = input(f"Player {player}, choose a space with row,col: ")
    ss = s.split(',')
    r=int(ss[0])
    c=int(ss[1])
    # whether (r,c) is empty or not
    while board[r][c]!='.':
        s = input(f"({r},{c}) is already chosen, Choose another space with row,col:")
        ss=s.split(',')
        r=int(ss[0])
        c=int(ss[1])
    board[r][c]=player

def initialize(n):
    board=[]
    for r in range(n):
        board.append([])
        for c in range(n):
            board[r].append('.')
    return board
def show(board):
    n=len(board)
    for r in range(n):
        for c in range(n):
            print(board[r][c],end="")
        print("")
def userinput(board,player):
    s=input(f"Player {player}, choose a space with row,col:")
    ss=s.split(',')
    r=int(ss[0])
    c=int(ss[1])
    # whether (r,c) is empty or not.
    while board[r][c]!='.': # when the space is not empty,
        s=input(f"({r},{c}) is already chosen, Choose another space with row,col:")
        ss=s.split(',')
        r=int(ss[0])
        c=int(ss[1])
    board[r][c]=player #direct mutation on board
def linechecker(L,player):
    n=len(L)
    for i in range(n):
        if L[i]!=player:
            return False
    return True
def winner(board,player):
    n=len(board)
    #n-row
    for r in range(0,n):
        L=[]
        for c in range(0,n):
            L.append(board[r][c])
        if linechecker(L,player):
            return True
    #n-col
    for c in range(0,n):
        L=[]
        for r in range(0,n):
            L.append(board[r][c])
        if linechecker(L,player):
            return True
    #diagonal1
    for r in range(0,n):
        L.append(board[r][r])
    if linechecker(L,player):
        return True
    #diagonal2
    for r in range(0,n):
        L.append(board[r][n-1-r])
    if linechecker(L,player):
        return True
    return False
# Make full until 11:04
def full(board):
    n=len(board)
    for r in range(0,n):
        for c in range(0,n):
            if board[r][c]==".": #empty!
                return False
    return True
def main():
    print("TIC-TAC-TOE")
    n=int(input("Type the size n:"))
    board=initialize(n)
    show(board)
    player="O"
    while True:
        userinput(board,player) #mutation on board
        show(board)
        if winner(board,player):
            print(f"{player} is the winner.")
            break
        elif full(board):
            print("Tie")
            break
        else: # switch the player
            if player=="O":
                player="X"
            else: #player="X"
                player="O"
if __name__ == "__main__":
    main()
