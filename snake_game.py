from typing import Optional
from game_display import GameDisplay
from new_class_try import Snake, Vertebra
class SnakeGame:

    def __init__(self) -> None:

        self.__key_clicked = 'Up'
        self.__snake = None
        self.__pre_move = 'Down'
        self.langh = 1
        self.key_change = {'Down': (-1, 0), 'Up': (1, 0), 'Right': (0, -1), 'Left': (0, 1)}
        self.back = {'Down': 'Up', 'Up': 'Down', 'Right': 'Left', 'Left': 'Right'}

    def insert_snake(self,args):
        self.__snake = Snake()
        self.__snake.snake_starter(3,args.width//2,args.height//2)


    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def get_cklike(self):
        return self.__key_clicked

    def update_objects(self)-> None:
        if (self.__key_clicked != self.back[self.__pre_move]):
            new_loc = (self.__snake.get_head().loc[0] + self.key_change[move_key][0],
                       self.__snake.get_head().loc[1] + self.key_change[move_key][1])
            self.__pre_move = self.__key_clicked
            self.__snake.move_snake(new_loc)



    def draw_board(self, gd: GameDisplay) -> None:

        current = self.__snake.get_head()
        while current is not None:
            gd.draw_cell(current.get_loc()[0], current.get_loc()[1], "blue")
            current = current.get_next()


    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return False

    #!!!!!