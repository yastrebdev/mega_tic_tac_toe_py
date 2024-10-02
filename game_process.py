import random

from functions.check_field import check_field
from functions.move_input import move_input
from utils.print_board import print_board


def game_process(*, players, board, fields):
    winner = False
    empty_cell = 81

    random_start_player = random.randint(0, 1)

    score = {
        'X': 0,
        'O': 0,
    }

    while not winner:
        player = players[random_start_player % 2]
        print(f'Ходит игрок {player.username}: {player.move_type}')
        print(f'Текущее поле {player.current_field}')

        open_fields = sum(sum(row) for row in fields)

        cell = move_input()
        if not cell: continue

        is_move = player.move(fields, board, cell)
        result = check_field(board, player.current_field, fields)
        if result:
            score[result] += 1

        if is_move:
            empty_cell -= 1
            random_start_player += 1
            print_board(board)

            is_field = players[random_start_player % 2].field_selection(fields, cell)
            if not is_field:
                print(f'Ходит игрок {players[random_start_player % 2].username}: {players[random_start_player % 2].move_type}')
                print('Текущее поле не определено')
            while not is_field:
                field = move_input()
                if not field:
                    continue
                is_field = players[random_start_player % 2].field_selection(fields, field)

        if score['X'] == 5:
            winner = 'X'
        elif score['O'] == 5:
            winner = 'O'

        if open_fields == 0:
            if score['X'] > score['O']:
                winner = 'X'
            elif score['O'] > score['X']:
                winner = 'O'
            else:
                break

        if empty_cell == 0:
            break

    if winner:
        return f'Выйграл {winner}!'
    else:
        return 'Ничья!'