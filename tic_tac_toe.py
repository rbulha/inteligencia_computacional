import sys
import getopt


def print_board(board):    
    board = ''.join(board)
    if len(board) == 9:
        print("           ")
        for line in range(3):
            line_str = ''
            line_bar = ['','|','|']
            for item in board[line*3:line*3+3]:
                if item.upper() == 'X':
                    line_str += ' X ' + line_bar.pop()
                elif item.upper() == 'O':
                    line_str += ' O ' + line_bar.pop()
                else:
                    line_str += '   ' + line_bar.pop()
            print(line_str)
            if line == 2:
                print("           ")
            else:    
                print("-----------")

def count_tic(board):
    return len([x for x in board if x.upper() =='X'])


def count_tac(board):
    return len([x for x in board if x.upper() =='O'])

def getsecondplayer(first):
    if first.upper() == 'X':
        return 'o'
    else:
        return 'x'

def solve_board(board,first='x'):
    try:
        index = board.index('_')
    except ValueError:
        index = -1
    if index >= 0:
        if (count_tic(board) + count_tac(board)) % 2 == 0:
            board[index]=first
        else:
            board[index]=getsecondplayer(first)
        return solve_board(board,first)    
    else:    
        return board

if __name__ == "__main__":
    argv = sys.argv[1:]
    first_player = 'x'
    verbose = False
    board = None
    try:
        opts, args = getopt.getopt(argv,"hf:b:v",["first=","board=","verbose="])
        for opt, arg in opts:
            if opt == '-h':
                print("%s -f x -b ____x____"%(__file__))
                sys.exit()
            elif opt in ("-f", "--first"):
                first_player = arg
            elif opt in ("-b", "--board"):
                if len(arg) == 9:
                    board = list(arg)
                else:
                    print("wrong board!")
            elif opt in ("-v", "--verbose"):
                verbose=True
        if board != None:
            result = solve_board(board,first_player)
            if verbose:
                print("first player = %s \n"%first_player)
                print_board(result)
            else:
                print(''.join(result))
    except getopt.GetoptError:
        print("%s -f x -b ____x____"%(__file__))
        sys.exit(2)

