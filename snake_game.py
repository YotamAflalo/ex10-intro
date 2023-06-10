from typing import Optional
from game_display import GameDisplay
from new_class_try import Snake, Vertebra
from ap_and_walls import Apples, Walls

class SnakeGame:

    def __init__(self) -> None:

        self.__key_clicked = 'Up'
        self.snake = Snake()
        self.__size = None
        self.__pre_move = 'Up'
        self.key_change = {'Down':(0, -1) , 'Up': (0, 1) , 'Right': (1, 0), 'Left':(-1, 0), None: (0,0)}
        self.back = {'Down': 'Up', 'Up': 'Down', 'Right': 'Left', 'Left': 'Right' , None: "____"}
        #
        #self.apple = {(1,1),(1,20),(0,0)}
        self.apple = Apples()
        self.wall = Walls()

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
                #self.snake.move_snake(new_loc, (False))
                self.snake.move_snake(new_loc,(new_loc in self.apple.ap_locs))
                if new_loc in self.apple.ap_locs:
                    self.apple.apple_remover(new_loc)
                self.wall.wall_move()
                if self.wall.need_more_walls():
                    self.wall.wall_generetor(self.wall.walls_loc,set(new_loc)) #יש פה טעות, צריך להכניס לו רשימה של מיקומי הנחש
                if self.apple.need_more_apple():
                    self.apple.apple_generetor(self.wall.walls_loc)



    def draw_board(self, gd: GameDisplay) -> None:
        current = self.snake.get_head()
        while current:
            #print(current.get_loc())
            gd.draw_cell(current.get_loc()[0], current.get_loc()[1], "black")
            current = current.prev
        #for appl in self.apple:
        #    gd.draw_cell(appl[0], appl[1], "green")
        for ap in self.apple.ap_locs:
            apx,apy = list(ap)[0],list(ap)[1]
            gd.draw_cell(apx, apy, "Green")
        for wall in self.wall.walls_loc.keys():
            for brick in self.wall.walls_loc[wall]:
                bx,by = brick[0],brick[1]
                if (0<brick[0]<self.__size[0]) and (0<brick[1]<self.__size[1]):
                    gd.draw_cell(bx, by, "Blue")
    def snake_len(self):
        return len(self.snake)



    def end_round(self) -> None:
        wall_ex_dict =self.wall.walls_loc.copy()
        for wall in wall_ex_dict.keys():
            out =1
            for brick in wall_ex_dict[wall]:
                if (0<brick[0]<self.__size[0]) and (0<brick[1]<self.__size[1]):
                    out=0
            if out==1:
                self.wall.wall_remove(wall)


    def is_over(self) -> bool:
        return False

    #!!!!!