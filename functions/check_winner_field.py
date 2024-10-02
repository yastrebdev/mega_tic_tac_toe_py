def check_cell(cell):
    if cell != '.':
        return cell
    else:
        return False


def check_winner_field(field):
    result = None
    for i in range(len(field)):
        if field[i][1] != '.' and field[i][0] == field[i][1] and field[i][1] == field[i][2]:
            result = field[i][0]
        elif field[1][i] != '.' and field[0][i] == field[1][i] and field[1][i] == field[2][i]:
            result = field[0][i]
        elif field[1][1] != '.' and field[0][0] == field[1][1] and field[1][1] == field[2][2]:
            result = field[0][0]
        elif field[1][1] != '.' and field[0][2] == field[1][1] and field[1][1] == field[2][0]:
            result = field[0][2]

    return result