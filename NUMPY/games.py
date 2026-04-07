import numpy as np

boards = np.zeros((3,3)).astype(int)

def print_board():
    symb = {0:" ", 1:"X", -1:"O"}
    for r in range(3):
        row = "|".join(symb[val] for val in boards[r])
        print(" " + row)
        if r < 2:
            print("---+---+---+")
    print()

print_board()




    



 