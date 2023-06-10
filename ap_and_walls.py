from typing import Optional
from game_display import GameDisplay
from new_class_try import Snake, Vertebra
from game_utils import *

class Apples:
    def __init__(self,max_num=3):
        self.max_num = max_num #כמות מקסימלית של תפוחים
        self.corrent_num = 0
        self.ap_locs = set() #נכניס לסט


    def apple_generetor(self,walls_loc:dict):
        new_apple_loc = get_random_apple_data() #tuple
        free_palce = 1
        if new_apple_loc in self.ap_locs:
            free_palce =0
        for key in walls_loc.keys():
            if new_apple_loc in walls_loc[key]:
                free_place = 0
        if free_palce==1:
            #כרגע הפונקציה לא מתחשבת בהתנגשות עם נחש או קיר. צריך לחשוב איפה להכניס את זה
            self.ap_locs.add(new_apple_loc)
            self.corrent_num = len(self.ap_locs)


    def apple_remover(self,loc:tuple):
        '''
        this func remove apple from the board. we will use it if
        :param loc: pace to remove apple from
        :return: nune
        '''
        self.ap_locs.remove(loc)
        self.corrent_num = len(self.ap_locs)

    def need_more_apple(self):
        return self.corrent_num<self.max_num

    def apple_wall_collision(self,wall_locs:dict):
        for ap_loc in self.ap_locs:
            for wall in wall_locs.keys():
                if ap_loc in wall_locs[wall]:
                    self.apple_remover(ap_loc)


class Walls:
    def __init__(self,max_num_walls = 2):
        self.walls_loc = {}
        self.max_walls =max_num_walls
        self.num_walls =0

    def wall_generetor(self,ap_locs:set,snake_locs:set):
        x_wall,y_wall,dir_wall = get_random_wall_data()
        key_change = {'Down': [-1, 0], 'Up': [1, 0], 'Right': [0, -1], 'Left': [0, 1]}
        free_place = 1
        for i in range(3):
            new_loc = x_wall+i*key_change[dir_wall][0],y_wall+i*key_change[dir_wall][1]
            if new_loc in ap_locs or new_loc in snake_locs:
                free_place=0
            for key in self.walls_loc.keys():
                if new_loc in self.walls_loc[key]:
                    free_place=0
        if free_place ==1:
            palce_list = [[x_wall+i*key_change[dir_wall][0],y_wall+i*key_change[dir_wall][1]] for i in range(3)]
            self.walls_loc[(x_wall,y_wall,dir_wall)] = palce_list
            self.num_walls+=1

    def wall_move(self):
        key_change = {'Down': [-1, 0], 'Up': [1, 0], 'Right': [0, -1], 'Left': [0, 1]}
        for wall in self.walls_loc.keys():
            #print(wall)
            #print(wall[-1])
            dir = wall[-1]
            for brick in self.walls_loc[wall]:
                brick[0]= brick[0]+key_change[dir][0]
                brick[1]=brick[1]+key_change[dir][1]

    def wall_remove(self,loc:tuple):
        self.walls_loc.pop(loc)
        self.num_walls -=1


    def wall_locs(self):
        return self.walls_loc

    def need_more_walls(self):
        return self.num_walls<self.max_walls


