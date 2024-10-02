import random


class Player:
    def __init__(self, *, username, move_type):
        self.username = username
        self.move_type = move_type
        self.current_field = random.randint(1, 9)


    def field_selection(self, fields, field: int):
        yf = (field - 1) // 3
        xf = (field - 1) % 3

        if fields[yf][xf] == 0:
            print(f'Поле закрыто, выберите другое >>>')
            return False
        else:
            self.current_field = field
            return True


    def move(self, fields, board, cell):
        field = self.current_field

        yf = (field - 1) // 3
        xf = (field - 1) % 3

        y = (cell - 1) // 3
        x = (cell - 1) % 3

        if board[yf][xf][y][x] == '.':
            board[yf][xf][y][x] = self.move_type
            fields[yf][xf] -= 1
            return True
        else:
            print(f'Здесь уже стоит {board[yf][xf][y][x]}')
            return False