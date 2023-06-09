from typing import Optional
from game_display import GameDisplay
from new_class_try import Snake, Vertebra

class SnakeGame:

    def __init__(self) -> None:

        self.__key_clicked = 'Up'
        self.snake = Snake()
        self.__size = None
        self.__pre_move = 'Up'
        self.key_change = {'Down':(0, -1) , 'Up': (0, 1) , 'Right': (1, 0), 'Left':(-1, 0), None: (0,0)}
        self.back = {'Down': 'Up', 'Up': 'Down', 'Right': 'Left', 'Left': 'Right' , None: "____"}



    def init_snake(self,size):
        self.__size = size
        self.snake.snake_starter(size[0]//2,size[1]//2)

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def get_cklike(self):
        #if self.__key_clicked == None:
         #   return self.__pre_move
        return self.__key_clicked

    def update_objects(self)-> None:
        #print("hed:",self.snake.get_head_loc())
        if self.__key_clicked == None:
            self.__key_clicked = self.__pre_move
        if (self.__key_clicked != self.back[self.__pre_move]):
            new_loc = self.snake.get_head_loc()[0] + self.key_change[self.__key_clicked][0],\
                self.snake.get_head_loc()[1] + self.key_change[self.__key_clicked][1]
            if  (0 <= new_loc[0] < self.__size[0]) and (0 <= new_loc[1] < self.__size[1]):
                self.__pre_move = self.__key_clicked
                self.snake.move_snake(new_loc)



    def draw_board(self, gd: GameDisplay) -> None:
        current = self.snake.get_head()
        while current:
            #print(current.get_loc())
            gd.draw_cell(current.get_loc()[0], current.get_loc()[1], "black")
            current = current.prev





    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return False

    #!!!!!