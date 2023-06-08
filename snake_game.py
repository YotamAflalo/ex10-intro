from typing import Optional
from game_display import GameDisplay
from new_class_try import Snake, Vertebra
class SnakeGame:

    def __init__(self) -> None:
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None
        self.__snake = None
        self.__pre_move = None
        self.langh = 1

    def insert_snake(self,args):
        self.__snake = Snake()
        self.__snake.snake_starter(3,args.width//2,args.height//2)
        #print(self.__snake.snake_locs()) #!

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def get_cklike(self):
        return self.__key_clicked

    def update_objects(self)-> None:
        if (self.__key_clicked == 'Left') and (self.__x > 0) and (self.__pre_move != "Right"):
            self.__snake.move_snake_left()
            #self.__x -= 1
            self.__pre_move = 'Left'
        elif (self.__key_clicked == 'Right') and (self.__x < 40) and (self.__pre_move != "Left"):
            self.__snake.move_snake_right()
            #self.__x += 1
            self.__pre_move = 'Right'
        elif (self.__key_clicked == 'Up') and (self.__y < 30) and (self.__pre_move != "Down"):
            #self.__y +=1
            self.__snake.move_snake_up()
            self.__pre_move ="Up"
        elif (self.__key_clicked == 'Down') and (self.__y > 0) and (self.__pre_move != "Up"):
            #self.__y -=1
            self.__snake.move_snake_down()
            self.__pre_move = "Down"
    def draw_board(self, gd: GameDisplay) -> None:
        current = self.__snake.get_head()
        while current is not None:
            gd.draw_cell(current.get_loc()[0], current.get_loc()[1], "blue")
            current = current.get_next()

        #gd.draw_cell(self.__x, self.__y, "blue")
        #gd.draw_cell(50,50,'red')

    def end_round(self) -> None:
        pass

    def is_over(self,args) -> bool:
        locs = self.__snake.get_head().get_loc
        #if locs[0]==0 or locs[0]==args.height//2 or locs[1]==0 or locs[1]==args.width//2:
        #    return True
        return False




