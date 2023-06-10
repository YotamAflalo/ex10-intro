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
        self.my_round = 0
        self.board_keep = (0,0)
        #
        #self.apple = {(1,1),(1,20),(0,0)}
        self.apple = Apples()
        self.wall = Walls()

    def init_objects(self, size, apple, walls):
        self.__size = size
        self.snake.snake_starter(size[0]//2,size[1]//2)
        self.apple.max_num=apple
        self.walls.max = walls

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
            self.board_keep = new_loc
            if  (0 <= new_loc[0] < self.__size[0]) and (0 <= new_loc[1] < self.__size[1]):
                self.__pre_move = self.__key_clicked
                #self.snake.move_snake(new_loc, (False))
                self.snake.move_snake(new_loc,(new_loc in self.apple.ap_locs))
                if new_loc in self.apple.ap_locs:
                    self.apple.apple_remover(new_loc)
                if self.my_round%2==0:
                    self.wall.wall_move()
                if self.wall.need_more_walls():
                    self.wall.wall_generetor(self.wall.walls_loc,self.snake.get_locs()) #יש פה טעות, צריך להכניס לו רשימה של מיקומי הנחש
                if self.apple.need_more_apple():
                    self.apple.apple_generetor(self.wall.walls_loc,self.snake.get_locs())
                ap_list = self.apple.ap_locs.copy()
                for wall in self.wall.walls_loc.keys():
                    for app_loc in ap_list:
                        if list(app_loc) in self.wall.walls_loc[wall]:
                            self.apple.apple_remover(app_loc)


                #חותכים נחש שנפגע מקיר
                loc_list = self.snake.get_locs()[1:]
                for wall in self.wall.walls_loc.keys():
                    for brick in self.wall.walls_loc[wall]:
                        if tuple(brick) in loc_list:
                            self.snake.cut_snake(tuple(brick))

    def draw_board(self, gd: GameDisplay) -> None:
        current = self.snake.get_head()
        while current:
            #print(current.get_loc())
            gd.draw_cell(current.get_loc()[0], current.get_loc()[1], "black")
            current = current.prev
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
        self.my_round +=1


    def is_over(self) -> bool:
        for wall in self.wall.walls_loc.keys():
            for brick in self.wall.walls_loc[wall]:
                if tuple(brick) == self.snake.get_head_loc():
                #if self.snake.collision(tuple(brick)):
                    print("Game over wall") #!
                    return True

        #התנגשות של ראש הנחש
        loc_list = self.snake.get_locs()
        if len(loc_list)!=len(set(loc_list)):
            print("Game over tail") #!
            return True


        if (self.board_keep[0] < 0) or (self.board_keep[1] < 0) \
                or (self.board_keep[0] > self.__size[0] - 1) or (self.board_keep[1] > self.__size[1] - 1):
            print("Game over board")
            return True
        return False

    #!!!!!!