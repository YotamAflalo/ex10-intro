from typing import Optional
from game_display import GameDisplay
from ap_and_walls import Apples, Walls
class SnakeGame:

    def __init__(self) -> None:
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None
        self.apple = Apples()
        self.wall = Walls()

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self)-> None:
        if (self.__key_clicked == 'Left') and (self.__x > 0):
            self.__x -= 1
            self.wall.wall_move()
            if self.wall.need_more_walls():
                self.wall.wall_generetor(self.wall.walls_loc)
            if self.apple.need_more_apple():
                self.apple.apple_generetor(self.wall.walls_loc)
        elif (self.__key_clicked == 'Right') and (self.__x < 40):
            self.__x += 1
            self.wall.wall_move()
            if self.wall.need_more_walls():
                self.wall.wall_generetor(self.wall.walls_loc)
            if self.apple.need_more_apple():
                self.apple.apple_generetor(self.wall.walls_loc)
        elif (self.__key_clicked == 'Up') and (self.__x < 40):
            self.__y += 1
            self.wall.wall_move()
            if self.wall.need_more_walls():
                self.wall.wall_generetor()
            if self.apple.need_more_apple():
                self.apple.apple_generetor()
        elif (self.__key_clicked == 'Down') and (self.__x < 40):
            self.__y -= 1
            self.wall.wall_move()
            if self.wall.need_more_walls():
                self.wall.wall_generetor()
            if self.apple.need_more_apple():
                self.apple.apple_generetor()

        snake_head_loc = (self.__x,self.__y) #צריך לרוץ על כל מיקומי הנחש
        if snake_head_loc in self.apple.ap_locs:
            self.apple.apple_remover(snake_head_loc)

    def draw_board(self, gd: GameDisplay) -> None:
        gd.draw_cell(self.__x, self.__y, "blue")
        for ap in self.apple.ap_locs:
            apx,apy = list(ap)[0],list(ap)[1]
            gd.draw_cell(apx, apy, "Green")
        for wall in self.wall.walls_loc.keys():
            for brick in self.wall.walls_loc[wall]:
                bx,by = brick[0],brick[1]
                gd.draw_cell(bx, by, "Blue")
    def end_round(self) -> None:
       pass


    def is_over(self) -> bool:
        return False