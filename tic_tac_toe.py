import math
import random
from copy import deepcopy
board=[[" " for _ in range(3)] for _ in range(3)]
def home():
    global toss
    global gamemode
    print("Welcome to Tic-Tac-Toe!\n")
    while True:
        start=int(input(("Shall we begin a game?\n1.Start \n2.Exit \n")))
        if start==1:
            toss=random.randint(1,2)
            while True:
                gamemode=int(input("Pls enter your gamemode choice:\n1.PvP \n2.PvE \n"))
                if gamemode==1:
                    PvPgamesetup()
                    break
                elif gamemode==2:
                    PvEgamesetup()
                    break
                else:
                    print("Wrong input!")
        elif start==2:
            break
        else:
            print("Wrong input!")
avl_moves = [(row, cell) for row in range(3) for cell in range(3)]
class Player:
    name=" "
    sign=" "
class ComputerPlayer():
    name="Computer"
    sign=" "
def is_full(board):
    ans=all(cell != " " for row in board for cell in row)
    return ans
def inputsign(sign):
        if gamemode==1:
            row=int(input("Enter row(1-3): "))
            col=int(input("Enter column(1-3): "))
            if playmove(row,col,sign)==0:
                print("Slot already full! Pls choose another slot!")
                inputsign(sign)
            else:
                playmove(row,col,sign)
        elif gamemode==2 and sign==P.sign:
            row=int(input("Enter row(1-3): "))
            col=int(input("Enter column(1-3): "))
            if playmove(row,col,sign)==0:
                print("Slot already full! Pls choose another slot!")
                inputsign(sign)
            else:
                playmove(row,col,sign)
        elif gamemode==2 and sign==C.sign:
            move=random.randrange(len(avl_moves))
            playmove(avl_moves[move][0]+1,avl_moves[move][1]+1,C.sign)
            print("Comptuer played a move!")
def check_win(board):
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]
        for col in range(3):
            if board[0][col]==board[1][col]==board[2][col] and board[0][col] != " ":
                return board[0][col]
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
            return board[0][2]
        return None
def PvPgamesetup():
    P1=Player()
    P2=Player()
    P1.name=input("Enter player 1's name: ")
    P2.name=input("Enter player 2's name: ")
    if toss==1:
        print(f"{P1.name} starts the game!")
        P1.sign="x"
        P2.sign="o"
        game(P1,P2)
    else:
        print(f"{P2.name} starts the game!")
        P2.sign="x"
        P1.sign="o"
        game(P2,P1)
def game(P1,P2):
    global end,gamewin
    gamewin=False
    lastinput=" "
    while (gamewin==False and is_full(board)==False):
        for row in range(3):
            for cell in range(3):
                if board[row][cell]==" ":
                    if (row,cell) not in avl_moves:
                        avl_moves.append((row,cell))
                else:
                    if (row,cell) in avl_moves:
                        avl_moves.remove((row,cell))
        for row in board:
            print(row)
        if lastinput==" " and toss==1:
            inputsign(P1.sign)
            lastinput=P1.sign
        elif lastinput==" " and toss==2:
            inputsign(P2.sign)
            lastinput=P2.sign
        elif lastinput==P1.sign:
            inputsign(P2.sign)
            lastinput=P2.sign
        else:
            inputsign(P1.sign)
            lastinput=P1.sign
        if check_win(board)==P1.sign:
            for row in board:
                print(row)
            print(f"{P1.name} Wins!")
            gamewin=True
            end=1
        elif check_win(board)==P2.sign:
            for row in board:
                print(row)
            print(f"{P2.name} Wins!")
            gamewin=True
            end=-1
    if is_full(board)==True and gamewin==False:
        for row in board:
            print(row)
        print("Game ended on a draw!")
        end=0
def playmove(rowin,colin,sign):
    if board[rowin-1][colin-1]==" ":
        board[rowin-1][colin-1]=sign
        print("Move made!")
        return 1
    else:
        return 0
def PvEgamesetup():
    global P,C
    P=Player()
    C=ComputerPlayer()
    P.name=input("Enter your name: ")
    if toss==1:
        print("You start the game!")
        P.sign="x"
        C.sign="o"
    else:
        print("Computer starts the game!")
        C.sign="x"
        P.sign="o"
    game(P,C)
home()