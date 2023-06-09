from typing import Optional
from game_display import GameDisplay
from new_class_try import Snake, Vertebra
from game_utils import *

class Apples:
    def __init__(self,max_num=3):
        self.max_num = max_num #כמות מקסימלית של תפוחים
        self.corrent_num = 0
        self.ap_locs = set() #נכניס לסט
    def apple_generetor(self,snake=None,walls= None):
        new_apple_loc = get_random_apple_data() #tuple
        if new_apple_loc not in self.ap_locs:
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



'''ap = Apples()

for i in range(0,10):
    if ap.need_more_apple():
        ap.apple_generetor()
        print(ap.ap_locs)
        print(ap.corrent_num)
locs = list(ap.ap_locs)
print("locs",locs)
for i in locs:
    ap.apple_remover(i)
    print(ap.ap_locs)
    print(ap.corrent_num)'''
