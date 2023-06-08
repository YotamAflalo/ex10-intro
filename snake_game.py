from typing import Optional
from game_display import GameDisplay
from new_class_try import Snake, Vertebra

class SnakeGame:

    def __init__(self) -> None:

        self.__key_clicked = 'Up'
        self.snake = Snake()
        self.__size = None
        self.__pre_move = 'Down'
        self.key_change = {'Down': (-1, 0), 'Up': (1, 0), 'Right': (0, -1), 'Left': (0, 1)}
        self.back = {'Down': 'Up', 'Up': 'Down', 'Right': 'Left', 'Left': 'Right'}

    def init_snake(self,size):
        self.__size = size
        self.snake.snake_starter(size[0]//2,size[1]//2)
        print(self.snake)

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def get_cklike(self):
        return self.__key_clicked

    def update_objects(self)-> None:
        if (self.__key_clicked != self.back[self.__pre_move]) and (self.snake.get_head() != None):
            new_loc = (self.snake.get_head_loc()[0] + self.key_change[self.__key_clicked][0],
                       self.snake.get_head_loc()[1] + self.key_change[self.__key_clicked][1])
            if  (0 <= new_loc[0] < self.__size[0]) and (0 <= new_loc[1] < self.__size[1]):
                self.__pre_move = self.__key_clicked
                self.snake.move_snake(new_loc)




    def draw_board(self, gd: GameDisplay) -> None:
        gd.draw_cell(15,15,'blue')
        current = self.snake.get_head()
        while current is not None:
            gd.draw_cell(current.get_loc()[0], current.get_loc()[1], "black")
            current = current.next





    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return False

    #!!!!!