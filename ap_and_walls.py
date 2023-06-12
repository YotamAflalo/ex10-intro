from typing import Optional
from game_display import GameDisplay
from new_class_try import Snake, Vertebra
from game_utils import *

class Apples:
    '''
    The apple class contain all the apples that exist in the game and their locations.
    '''
    def __init__(self, max_num=3):
        self.max_num = max_num  # maximum number of apples
        self.corrent_num = 0
        self.ap_locs = set()  # set to store apple locations


    def apple_generetor(self, walls_loc: dict, snake_locs: list):
        '''

        :param walls_loc: dict of walls locations
        :param snake_locs: list of snake location
        :return: None
        '''
        new_apple_loc = get_random_apple_data()  # generates a random apple location (tuple)
        free_place = 1
        # Check if the new apple location is already occupied by another apple
        if new_apple_loc in self.ap_locs:
            free_place = 0
        # Check if the new apple location is in any of the walls
        for key in walls_loc.keys():
            if new_apple_loc in walls_loc[key]:
                free_place = 0
        # Check if the new apple location is in the snake's body
        if new_apple_loc in snake_locs:
            free_place = 0
        # If the location is free, add the new apple to ap_locs and update the current number of apples
        if free_place == 1:
            self.ap_locs.add(new_apple_loc)
            self.corrent_num = len(self.ap_locs)

    def apple_remover(self,loc:tuple):
        '''
        this func remove apple from the board. we will use it if
        :param loc: pace to remove apple from
        :return: None
        '''
        try:
            self.ap_locs.remove(loc)
            self.corrent_num = len(self.ap_locs)
        except KeyError:
            None

    def need_more_apple(self):
        '''
        :return: if more apple ar needed
        '''
        return self.corrent_num<self.max_num

    def apple_wall_collision(self,wall_locs:dict):
        '''
        chack if apple and wall collided. if so - dalete the apple
        :param wall_locs: dict of walls locations
        :return: None
        '''
        for ap_loc in self.ap_locs:
            for wall in wall_locs.keys():
                if ap_loc in wall_locs[wall]:
                    # If there is a collision, remove the apple
                    self.apple_remover(ap_loc)


class Walls:
    '''
    The Walls object contain all the apples that exist in the game and their locations.
    '''
    def __init__(self,max_num_walls = 2):
        self.walls_loc = {}
        self.max_walls =max_num_walls
        self.num_walls =0

    def wall_generetor(self,ap_locs:set,snake_locs:set):
        '''
        generate a new wall
        :param ap_locs: apple locations in set
        :param snake_locs: snake locations in list
        :return: None
        '''
        x_wall,y_wall,dir_wall = get_random_wall_data()
        #key_change = {'Down': [-1, 0], 'Up': [1, 0], 'Right': [0, -1], 'Left': [0, 1]}
        key_change = {'Right': [1, 0], 'Left': [-1, 0], 'Down': [0, -1], 'Up': [0, 1]}
        free_place = 1
        for i in range(-1,2,1): #generate wall with 3 bricks
            new_loc = x_wall+i*key_change[dir_wall][0],y_wall+i*key_change[dir_wall][1]
            #chack for apples
            if new_loc in ap_locs or new_loc in snake_locs:
                free_place=0
            #chack for aother walls
            for key in self.walls_loc.keys():
                if new_loc in self.walls_loc[key]:
                    free_place=0
        if free_place ==1:
            #making list with all the brick places
            palce_list = [[x_wall+j*key_change[dir_wall][0],y_wall+j*key_change[dir_wall][1]] for j in range(-1,2,1)]
            self.walls_loc[(x_wall,y_wall,dir_wall)] = palce_list #place the new wall
            self.num_walls+=1 #add 1 to the walls count

    def wall_move(self):
        '''
        move the walls one block in their direction
        :return: None
        '''
        #key_change = {'Down': [-1, 0], 'Up': [1, 0], 'Right': [0, -1], 'Left': [0, 1]}
        key_change = {'Right': [1, 0], 'Left': [-1, 0], 'Down': [0, -1], 'Up': [0, 1]}
        # Move each wall in the right direction, by the keys above
        for wall in self.walls_loc.keys():

            dir = wall[-1] #the direction of the move
            for brick in self.walls_loc[wall]:
                brick[0]= brick[0]+key_change[dir][0]
                brick[1]=brick[1]+key_change[dir][1]

    def wall_remove(self,loc:tuple):
        '''
        remove wall that his head is at "loc" cordinate
        :param loc: wall's head cordinate
        :return: None
        '''
        self.walls_loc.pop(loc)
        self.num_walls -=1


    def wall_locs(self):
        '''
        :return: dict with the locations of all the wals
        '''
        return self.walls_loc

    def need_more_walls(self):
        '''
        :return: if new walls are needed.
        '''
        return self.num_walls<self.max_walls


