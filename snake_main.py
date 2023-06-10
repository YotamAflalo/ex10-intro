import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay
from new_class_try import Snake

def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:
    # INIT OBJECTS
    game = SnakeGame()
    gd.show_score(0)
    unpack_arg = {**vars(args)}
    print(unpack_arg)
    size = (unpack_arg['width'],unpack_arg['height'])
    rounds = unpack_arg['rounds']
    game.init_objects(size,unpack_arg['apples'],unpack_arg['walls'])

    # DRAW BOARD
    game.draw_board(gd)
    # END OF ROUND 0
    while not game.is_over():

        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)
        # UPDATE OBJECTS
        game.update_objects()
        a = (game.snake_len() ** 0.5) // 1
        gd.show_score(int(a))

        # DRAW BOARD
        game.draw_board(gd)
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()


if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")
    #1