from typing import Optional
from game_display import GameDisplay
from new_class_try import Snake, Vertebra
from ap_and_walls import Apples, Walls

class SnakeGame:
    '''
    A snake game is an object that contains all the components for managing a snake game.
    '''

    def __init__(self) -> None:
        """
        A constructor for a SnakeGame object.

        """
        self.__key_clicked = None
        self.snake = Snake()
        self.apple = Apples()
        self.wall = Walls()
        self.color = 'black'
        self.__size = None
        self.__pre_move = 'Up'
        self.key_change = {'Down':(0, -1) , 'Up': (0, 1) , 'Right': (1, 0), 'Left':(-1, 0), None: (0,0)}
        self.back = {'Down': 'Up', 'Up': 'Down', 'Right': 'Left', 'Left': 'Right' , None: "____"}
        self.my_round = 0
        self.board_keep = (0,0)


    def init_objects(self, size, apple, walls):
        """
        Receives data from the main
        regarding the running conditions.
        :param size: The size of the board in tuples
        :param apple: max amount of apples
        :param walls: max amount of walls
        :return:None
        """
        self.__size = size
        self.snake.snake_starter(size[0]//2,size[1]//2)
        self.apple.max_num=apple
        self.wall.max_walls = walls


    def init_objects_debug(self, size, apple, walls):
        """
        Receives data from the main
        regarding the running conditions.
        bild the game with a ghost snake.
        :param size: The size of the board in tuples
        :param apple: max amount of apples
        :param walls: max amount of walls
        :return:None
        """
        self.__size = size
        self.snake.snake_starter((size[0]//2) - 0.5, (size[1]//2) - 0.5)
        self.color = 'white'
        self.apple.max_num=apple
        self.wall.max_walls = walls
    def read_key(self, key_clicked: Optional[str])-> None:
        """
        Read the key that the user pressed
        """
        self.__key_clicked = key_clicked

    def get_cklike(self):
        """
        Gets the key that the user pressed
        """
        return self.__key_clicked

    def update_objects(self)-> None:
        """
        Updates all the objects placed on the board
        """

    #For the sake of continuous running the game will treat not clicking as the previous click.
        if self.__key_clicked == None:
            self.__key_clicked = self.__pre_move
    # Checks if the direction is not the opposite direction from the previous reading.
    # If so it will ignore the current reading.
    # Configer the new location the had suld go to.
        if (self.__key_clicked != self.back[self.__pre_move]):
            new_loc = self.snake.get_head_loc()[0] + self.key_change[self.__key_clicked][0],\
                self.snake.get_head_loc()[1] + self.key_change[self.__key_clicked][1]
            self.board_keep = new_loc
        else:
            new_loc = self.snake.get_head_loc()[0] + self.key_change[self.__pre_move][0],\
                self.snake.get_head_loc()[1] + self.key_change[self.__pre_move][1]
            self.__key_clicked = self.__pre_move
            self.board_keep = new_loc

    # Update data on the class.
        if  (0 <= new_loc[0] < self.__size[0]) and (0 <= new_loc[1] < self.__size[1]):
            self.__pre_move = self.__key_clicked
            self.snake.move_snake(new_loc,(new_loc in self.apple.ap_locs))

    # Objects interaction:
        if new_loc in self.apple.ap_locs: #if apple got eat
            self.apple.apple_remover(new_loc)
        if self.my_round%2==0: #if need to move the whalls
            self.wall.wall_move()
        if self.wall.need_more_walls():
            self.wall.wall_generetor(self.wall.walls_loc,self.snake.get_locs())
        if self.apple.need_more_apple():
            self.apple.apple_generetor(self.wall.walls_loc,self.snake.get_locs())
        ap_list = self.apple.ap_locs.copy()
        for wall in self.wall.walls_loc.keys():
            for app_loc in ap_list:
                if list(app_loc) in self.wall.walls_loc[wall]:
                    self.apple.apple_remover(app_loc)
                    break

                # If a wall is run over by a snake
                loc_list = self.snake.get_locs()[1:]
                for wall in self.wall.walls_loc.keys():
                    for brick in self.wall.walls_loc[wall]:
                        if tuple(brick) in loc_list:
                            self.snake.cut_snake(tuple(brick))


    def draw_board(self, gd: GameDisplay) -> None:
        """
        Gets all the locations to display on the board and sends them to the display function
        """
        current = self.snake.get_head()
        while current and self.color == 'black':
            gd.draw_cell(current.get_loc()[0], current.get_loc()[1], 'black')
            current = current.prev
        for ap in self.apple.ap_locs:
            apx,apy = list(ap)[0],list(ap)[1]
            gd.draw_cell(apx, apy, "green")
        for wall in self.wall.walls_loc.keys():
            for brick in self.wall.walls_loc[wall]:
                bx,by = brick[0],brick[1]
                if (0 <= brick[0]<self.__size[0]) and (0 <= brick[1] < self.__size[1]):
                    gd.draw_cell(bx, by, "blue")

    def snake_len(self):
        return len(self.snake)

    def end_round(self) -> None:
        '''
        In this code section we check whether a wall has left the board.
         If so - we remove it from the dict of walls
        '''
        wall_ex_dict =self.wall.walls_loc.copy()
        for wall in wall_ex_dict.keys():
            out =1
            for brick in wall_ex_dict[wall]:
                if (0<=brick[0]<=self.__size[0]) and (0<=brick[1]<=self.__size[1]):
                    out=0
            if out==1:
                self.wall.wall_remove(wall)
        self.my_round +=1


    def is_over(self) -> bool:
        """
        Checks if the player has lost
        """
        # Collision with the wall
        for wall in self.wall.walls_loc.keys():
            for brick in self.wall.walls_loc[wall]:
                if tuple(brick) == self.snake.get_head_loc():
                    print("Game over wall")
                    return True

        #self eating
        loc_list = self.snake.get_locs()
        #print((loc_list),'\n',(set(loc_list)))
        if len(loc_list) != len(set(loc_list)):
            print("Game over tail")
            return True

        #Hitting the board boundaries
        if self.color == 'black':
            if (self.board_keep[0] < 0) or (self.board_keep[1] < 0) \
                    or (self.board_keep[0] > self.__size[0] - 1) or (self.board_keep[1] > self.__size[1] - 1):
                print("Game over board")
                return True
        return False

