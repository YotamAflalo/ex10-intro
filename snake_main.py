import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay

def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:
    # INIT OBJECTS
    game = SnakeGame()
    gd.show_score(0)
    unpack_arg = {**vars(args)}
    #print(unpack_arg)
    size = (unpack_arg['width'],unpack_arg['height'])
    rounds = unpack_arg['rounds']
    if rounds > 0:
        rounds += 1
    if unpack_arg['debug'] == False:
        game.init_objects(size,unpack_arg['apples'],unpack_arg['walls'])
    else:
        game.init_objects_debug(size,unpack_arg['apples'],unpack_arg['walls'])
    # DRAW BOARD
    game.update_appels_and_walls()
    game.draw_board(gd)
    # END OF ROUND 0
    gd.end_round()
    while (not game.is_over()) and not rounds in [0,1]:
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)
        # UPDATE OBJECTS
        game.update_objects()

        # DRAW BOARD
        gd.show_score(game.snake.score)

        game.draw_board(gd)
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()
        rounds -= 1


if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")
