from Player import Player
from game_process import game_process

fields = [[9] * 3 for _ in range(3)]

board = [[[['.', '.', '.']
           for _ in range(3)]
          for _ in range(3)]
         for _ in range(3)]

player_x = Player(username='Bob', move_type='X')
player_o = Player(username='Jon', move_type='O')

match_players = [player_x, player_o]

winner = game_process(players=match_players, board=board, fields=fields)
print(winner)