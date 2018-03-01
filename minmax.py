import sys
import time
import getopt
from tic_tac_toe import print_board
from tic_tac_toe import getsecondplayer

def checkwinner(b, player):
    if (b[0] == b[1] == b[2] == player) or \
        (b[3] == b[4] == b[5] == player) or \
        (b[6] == b[7] == b[8] == player) or \
        (b[0] == b[3] == b[6] == player) or \
        (b[1] == b[4] == b[7] == player) or \
        (b[2] == b[5] == b[8] == player) or \
        (b[0] == b[4] == b[8] == player) or \
        (b[2] == b[4] == b[6] == player):
            return True
    else:
        return False

def checkspace(board,player):
    if len([t for t in board if t==player]) == 2:
        try:
            nextmove = board.index('_')
            return nextmove
        except ValueError:
            return -1
    else:
        return -1

def checknextmovewinner(b,player):
    for i in range(0,7,3):
        b1 = b[i:i+3]
        nextmove = checkspace(b1,player)
        if nextmove >= 0:
            return i+nextmove

    for i in range(3):
        b1 = [b[i],b[i+3],b[i+6]]
        nextmove = checkspace(b1,player)
        if nextmove >= 0:
            m = [i,i+3,i+6]
            return m[nextmove]

    b1 = [b[0],b[4],b[8]]
    nextmove = checkspace(b1,player)
    if nextmove >= 0:
        m = [0,4,8]
        return m[nextmove]
    else:
        b1 = [b[2],b[4],b[6]]
        nextmove = checkspace(b1,player)
        if nextmove >= 0:
            m = [2,4,6]
            return m[nextmove]
        else:
            return -1

def score(winner,maxp):
    if winner == maxp:
        return 1
    elif winner == 'n':
        return 0
    else:
        return -1

def solve_minmax(board,maxp,player,root):
    global deepth
    deepth += 1

    solution = []
    for i,p in enumerate(board):
        if p == '_':
            b1 = []
            b1.extend(board)
            b1[i]=player
            if checkwinner(b1, player):
                if player == maxp:
                    solution.append(1)
                else:
                    solution.append(-1)
                return solution

    solution = []
    for i,p in enumerate(board):
        if p == '_':
            b1 = []
            b1.extend(board)
            b1[i]=player
            solution_node = solve_minmax(b1,maxp,getsecondplayer(player),False)
            if player != maxp:
                solution.append(max(solution_node))
            else:
                solution.append(min(solution_node))

    if len(solution) == 0: #draw
        solution.append(0)
    return solution
    '''
    nextmove = checknextmovewinner(board,player)
    if nextmove >= 0: #winning move
        b1 = []
        b1.extend(board)
        b1[nextmove] = player
        solution[nextmove] = 1
    else:
        nextmove = checknextmovewinner(board,getsecondplayer(player))
        if nextmove >= 0: #must go move
            b1 = []
            b1.extend(board)
            b1[nextmove] = player
            solution[nextmove] = 1
        else:
        board.index('_')
        for i,p in enumerate(board):
            if p == '_':
                b1 = []
                b1.extend(board)
                b1[i]=player
                winner = checkwinner(b1)
                if winner == maxp:
                    solution[i] = 1
                elif:
                    solution[i] = solve_minmax(b1,maxp,getsecondplayer(player),False)
    except ValueError:
        #print_board(board)
        #print(score(checkwinner(board),maxp))
        return score(checkwinner(board),maxp)
    if root:
        return solution
    elif player == maxp:
        #print(solution)
        return max(solution)
    else:
        return min(solution)
    '''

#print(score(checkwinner(['x','o','x','o','x','o','x','o','x']),'x'))
#print(score(checkwinner(['x','o','x','o','x','o','x','o','x']),'o'))
#print(solve_minmax(['x','o','x','o','x','o','x','_','_'],'x','x',True))
#print(solve_minmax(['_','_','_','_','_','_','_','_','_'],'x','x',True))

def picknextmove(board,result,maxp):
    possiblemoves = [i for i,t in enumerate(board) if t=='_']
    if len(possiblemoves) > 0:
        for i,pos in enumerate(possiblemoves):
            if result[i] == 1:
                board[pos] = maxp
                return board
        for i,pos in enumerate(possiblemoves):
            if result[i] == 0:
                board[pos]= maxp
                return board
        board[possiblemoves[0]]= maxp
        return board
    else:
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
            if verbose:
                print_board(board)
            ts = time.time()
            result = solve_minmax(board,maxp,first_player,True)
            if verbose:
                print("time = %0.6f sec  depth=%d"%((time.time() - ts),deepth))
                print("first player = %s result=%r \n"%(first_player,result))
                board = picknextmove(board,result,maxp)
                print_board(board)
                print(''.join(board))
            else:
                print(result)
    except getopt.GetoptError:
        print("%s -f x -b ____x____"%(__file__))
        sys.exit(2)




