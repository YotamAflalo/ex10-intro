from typing import Optional
from game_display import GameDisplay

class SnakeGame:

    def __init__(self) -> None:
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None
        self.__pre_move = None
        self.langh = 1

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def get_cklike(self):
        return self.__key_clicked

    def update_objects(self)-> None:
        if (self.__key_clicked == 'Left') and (self.__x > 0) and (self.__pre_move != "Right"):
            self.__x -= 1
            self.__pre_move = 'Left'
        elif (self.__key_clicked == 'Right') and (self.__x < 40) and (self.__pre_move != "Left"):
            self.__x += 1
            self.__pre_move = 'Right'
        elif (self.__key_clicked == 'Up') and (self.__y < 40) and (self.__pre_move != "Down"):
            self.__y +=1
            self.__pre_move ="Up"
        elif (self.__key_clicked == 'Down') and (self.__y > 0) and (self.__pre_move != "Up"):
            self.__y -=1
            self.__pre_move = "Down"
    def draw_board(self, gd: GameDisplay) -> None:
        gd.draw_cell(self.__x, self.__y, "blue")

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return False



"""sg = SnakeGame
i = 0
l = []
while i<10:
    i"""
