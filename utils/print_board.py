def print_board(board):
    for big_row in board:
        for small_row in range(3):
            print(" | ".join(" ".join(big_row[col][small_row]) for col in range(3)))
        print("- - - -" * 3)