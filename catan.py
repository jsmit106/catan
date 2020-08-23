# Generates a random layout for a Catan board
#
# @author   James Smith (jsmit106@asu.edu)
from random import shuffle

columns = 11

resources = {
    'wheat': 13,
    'wood': 12,
    'ore': 12,
    'brick': 12,
    'sheep': 12,
    'desert': 4,
}

numbers = {
    '2': 5,
    '3': 6,
    '4': 7,
    '5': 7,
    '6': 6,
    '8': 6,
    '9': 7,
    '10': 7,
    '11': 6,
    '12': 4,
}

board = [
    [[None, None] for _ in range(0, (columns - 3))],
    [[None, None] for _ in range(0, (columns - 2))],
    [[None, None] for _ in range(0, (columns - 1))],
    [[None, None] for _ in range(0, (columns))],
    [[None, None] for _ in range(0, (columns - 1))],
    [[None, None] for _ in range(0, (columns - 2))],
    [[None, None] for _ in range(0, (columns - 3))],
]

R = []
for r in resources.keys():
    R += [r for _ in range(0, resources[r])]

N = []
for n in numbers.keys():
    N += [n for _ in range(0, numbers[n])]

assert len(R) == len(N) + resources['desert']

shuffle(R)
shuffle(N)

#######################################
# Imperative Solution
#######################################
def lst_rem(x, L):
    return L[:L.index(x)] + L[L.index(x)+1:]

# we specify two spaces which must contain a wood resource
idx = R.index('wood')
board[3][0][0] = R[idx]

idx = R.index('wood')
board[3][columns-1][0] = R[idx]

# @yield    rem_R, rem_N
def fill_row(R, N, board, row, col):
    if col == len(board[row]):
        yield R, N
    
    else:  # col < len(board[row])
        tried_R = {}
        for r in R:
            if r in tried_R:
                continue
            else:
                tried_R[r] = True

            if board[row][col][0] != None and board[row][col][0] != r:
                continue
            if r == 'desert':
                board[row][col][0] = r
                board[row][col][1] = '0'
                new_R = lst_rem(r, R)

                iter = fill_row(new_R, N, board, row, col+1)

                for rem_R, rem_N in iter:
                    yield rem_R, rem_N
            
            else: # r != 'desert'
                board[row][col][0] = r
                new_R = lst_rem(r, R)
                tried_N = {}

                for n in N:
                    if n in tried_N:
                        continue
                    else:
                        tried_N[n] = True

                    if col > 0 and board[row][col-1][1] == n:
                        continue
                    if row < 3 and (board[row+1][col][1] == n or board[row+1][col+1][1] == n):
                        continue
                    if row > 3 and (board[row-1][col][1] == n or board[row-1][col+1][1] == n):
                        continue

                    board[row][col][1] = n
                    new_N = lst_rem(n, N)

                    iter = fill_row(new_R, new_N, board, row, col+1)

                    for rem_R, rem_N in iter:
                        yield rem_R, rem_N
                        
                board[row][col][1] = None
            
        board[row][col][0] = None
        board[row][col][1] = None

# @yield    success
def fill_table(R,N, board):
    row_3 = fill_row(R, N, board, 3, 0)

    for r3, n3 in row_3:
        row_2 = fill_row(r3, n3, board, 2, 0)

        for r2, n2 in row_2:
            row_1 = fill_row(r2, n2, board, 1, 0)

            for r1, n1 in row_1:
                row_0 = fill_row(r1, n1, board, 0, 0)

                for r0, n0 in row_0:
                    row_4 = fill_row(r0, n0, board, 4, 0)

                    for r4, n4 in row_4:
                        row_5 = fill_row(r4, n4, board, 5, 0)

                        for r5, n5 in row_5:
                            row_6 = fill_row(r5, n5, board, 6, 0)

                            for _, _ in row_6:
                                yield True
                            
                            print(r5)
                            print(n5)

iter = fill_table(R, N, board)
if iter.__next__():
    for row in board:
        print(row)
