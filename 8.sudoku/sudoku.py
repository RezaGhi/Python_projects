from pprint import pprint


from pprint import pprint
def find_next_empty(puzzle):

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    
    return None,None

def is_valid(puzzle,guess,row,col):

    row_vals=puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals=[puzzle[i][col] for i in range(9)]
    
    if guess in col_vals:
        return False

    start_rows = (row//3)*3
    start_cols = (col//3)*3

    for r in range(start_rows,start_rows+3):
        for c in range(start_cols,start_cols+3):
            if puzzle[r][c] == guess:
                return False
    
    return True

def sudoku_solver(puzzle):


    row , col = find_next_empty(puzzle)

    if row is None:
        return True
    
    for guess in range(1,10):
        
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col]=guess
            
            if sudoku_solver(puzzle):
                return True

        puzzle[row][col]=-1
    
    return False


example_board=[
    [-1,-1,-1,  2,-1,-1,  -1,-1,3],
    [-1,6,-1,   -1,-1,-1,  -1,-1,-1],
    [4,5,-1,    -1,-1,-1,  -1,2,-1],
    
    [8,4,-1,    -1,-1,5,   -1,-1,9],
    [-1,-1,3,   -1,8,-1,   -1,-1,-1],
    [-1,-1,6,   -1,-1,-1,  -1,4,-1],

    [-1,-1,8,   -1,-1,-1,  -1,-1,-1],
    [-1,-1,-1,   -1,-1,9,  7,-1,-1],
    [1,2,-1,     -1,5,-1,  -1,3,-1]
]

example_board2=[
    [7,-1,-1,   -1,5,-1,   6,4,-1],
    [-1,4,-1,   -1,-1,-1,  -1,-1,3],
    [-1,-1,-1,   6,-1,-1,  -1,-1,8],

    [-1,-1,-1,  -1,-1,-1,  -1,3,-1],
    [8,-1,-1,   -1,-1,1,   -1,-1,-1],
    [-1,1,-1,   2,-1,-1,    4,5,-1],
    
    [-1,-1,-1,  -1,-1,-1,   -1,-1,6],
    [-1,8,-1,    5,-1,-1,    2,1,-1],
    [-1,-1,9,    -1,7,-1,   -1,-1,-1]
]

print(sudoku_solver(example_board2))
pprint(example_board2)