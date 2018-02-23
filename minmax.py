import sys
import time
import getopt
from tic_tac_toe import print_board
from tic_tac_toe import getsecondplayer

def checkwinner(b):
    winner = 'd'
    if b[0] == b[1] == b[2]:
        winner = b[0]
    elif b[3] == b[4] == b[5]:
        winner = b[3]
    elif b[6] == b[7] == b[8]:
        winner = b[6]
    elif b[0] == b[3] == b[6]:
        winner = b[0]
    elif b[1] == b[4] == b[7]:
        winner = b[1]
    elif b[2] == b[5] == b[8]:
        winner = b[2]
    elif b[0] == b[4] == b[8]:
        winner = b[0]
    elif b[2] == b[4] == b[6]:
        winner = b[2]
    return winner

def score(winner,maxp):
    if winner == maxp:
        return 1
    elif winner == 'd':
        return 0
    else:
        return -1

def solve_minmax(board,maxp,player,root):
    global deepth
    solution = [0,0,0,0,0,0,0,0,0]
    try:
        board.index('_')
        for i,p in enumerate(board):
            if p == '_':
                b1 = []
                b1.extend(board)
                b1[i]=player
                deepth += 1
                solution[i] = solve_minmax(b1,maxp,getsecondplayer(player),False)
            elif root:
                solution[i] = p
        if root:
            return solution
        elif player == maxp:
            #print(solution)
            return max(solution)
        else:
            return min(solution)
    except ValueError:
        #print_board(board)
        #print(score(checkwinner(board),maxp))
        return score(checkwinner(board),maxp)

#print(score(checkwinner(['x','o','x','o','x','o','x','o','x']),'x'))
#print(score(checkwinner(['x','o','x','o','x','o','x','o','x']),'o'))
#print(solve_minmax(['x','o','x','o','x','o','x','_','_'],'x','x',True))
#print(solve_minmax(['_','_','_','_','_','_','_','_','_'],'x','x',True))

def picknextmove(board,result,maxp):
    if len([ t for t in result if t == 0]) == 9: #all draw
        board[4]=maxp
    elif len([ t for t in result if t == 1]) == 9: #all wins
        board[4]=maxp
    elif len([ t for t in result if t == -1]) == 9: #all loses
        board[4]=maxp
    elif len([ t for t in result if t == 1]) > 0: #chance to win
        pos = result.index(1)
        board[pos]=maxp
    elif len([ t for t in result if t == 0]) > 0: #chance to draw
        pos = result.index(0)
        board[pos]=maxp
    return board

if __name__ == "__main__":
    argv = sys.argv[1:]
    first_player = 'x'
    maxp = 'x'
    verbose = False
    board = None
    deepth = 0
    try:
        opts, args = getopt.getopt(argv,"hf:m:b:v",["first=","maxp=","board=","verbose="])
        for opt, arg in opts:
            if opt == '-h':
                print("%s -f x -b ____x____"%(__file__))
                sys.exit()
            elif opt in ("-f", "--first"):
                first_player = arg
                maxp = arg
            elif opt in ("-b", "--board"):
                if len(arg) == 9:
                    board = list(arg)
                else:
                    print("wrong board!")
            elif opt in ("-v", "--verbose"):
                verbose=True
        if board != None:
            ts = time.time()
            result = solve_minmax(board,maxp,first_player,True)
            if verbose:
                print("time = %0.6f sec  deepth=%d"%((time.time() - ts),deepth))
                print("first player = %s \n"%first_player)
                print(result)
                board = picknextmove(board,result,maxp)
                print_board(board)
                print(''.join(board))
            else:
                print(result)
    except getopt.GetoptError:
        print("%s -f x -b ____x____"%(__file__))
        sys.exit(2)




