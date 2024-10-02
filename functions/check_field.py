from functions.check_winner_field import check_winner_field


def check_field(board, field, fields):
    yf = (field - 1) // 3
    xf = (field - 1) % 3

    winner_field = check_winner_field(board[yf][xf])

    if not winner_field:
        return False
    else:
        fields[yf][xf] = 0
        return winner_field