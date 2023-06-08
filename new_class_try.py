class Vertebra:

    def __init__(self,loc, next=None, prev= None):
        self.loc = loc
        self.next = next
        self.prev = prev


    def get_loc(self):
        return (self.loc)

    def get_next(self):
        return self.next

    def set_loc(self,x,y):
        self.loc = loc = y

    def set_next(self,next):
        self.next = next


class Snake:
    ITEM_NOT_FOUND = -1
    def __init__(self, head=None):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def snake_starter(self, num, row, col):
        '''
        start a snake with "nam" Vertebras, with head at row,col

        '''
        for i in range(1,num+1):
            loc = (row-num+i,col)
            ver = Vertebra(loc)
            self.add_first(ver)


    def get_head(self):
        return self.__head

    def is_empty(self):
        return self.__head == None

    def add_first(self, vertebra):
        if self.__head is None:
            # list was empty
            self.__tail = vertebra
        else:
            self.__head.prev = vertebra
            vertebra.next = self.__head
        # update head
        self.__head = vertebra
        self.__length += 1

    def pop_lest(self):
        '''
        drop the lest vertebra of the snake
        :return: the lest vertebra location
        '''
        loc  = self.__tail.get_loc()

        self.__tail = self.__tail.prev
        if self.__tail is None:  # list is now empty
            self.__head = None
        else:  # disconnect old tail
            self.__tail.next.prev = None
        self.__tail.next = None
        self.__length -= 1
        return loc

    def move_snake(self, loc, apple=False):
        new_vertebra = Vertebra(loc)
        self.add_first(new_vertebra)
        if apple == False:
            self.pop_lest()
        else:
            self.__length += 1
    #def move_snake_left(self, apple = False):
     #   new_vertebra = Vertebra(loc=(self.__head.get_loc()[0]-1,self.__head.get_loc()[1]))
      #  self.add_first(new_vertebra)
    #    if apple==True:
    #        self.__length +=1
    #    else:
    #        self.pop_lest()


    #def move_snake_right(self, apple = False):

    #    new_vertebra = Vertebra(loc=(self.__head.get_loc()[0] + 1, self.__head.get_loc()[1]))
    #    self.add_first(new_vertebra)
    #    if apple == True:
    #        self.__length += 1
    #    else:
    #        self.pop_lest()


    #def move_snake_up(self, apple = False):
    #    new_vertebra = Vertebra(loc=(self.__head.get_loc()[0],self.__head.get_loc()[1]+1))
    #    self.add_first(new_vertebra)
    #    if apple == True:
    #        self.__length += 1
    #    else:
    #        self.pop_lest()


    #def move_snake_down(self, apple = False):
    #    new_vertebra = Vertebra(loc=(self.__head.get_loc()[0], self.__head.get_loc()[1]-1))
    #    self.add_first(new_vertebra)
    #    if apple == True:
    #        self.__length += 1
    #    else:
    #        self.pop_lest()


    def __len__(self):
        current = self.__head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count


    def collision(self, loc):
        '''

        :param loc: place of the new head of the snale
        :return: if there is a collision with his own tail
        '''
        if self.collision_helper(self.__head, loc, 0) == -1:
            return False
        else: return True


    def collision_helper(self, cur, loc, index):
        if index >= self.__len__():
            return -1

        if cur.get_loc() == loc:
            return index
        return self.collision_helper(cur.get_next(), loc,index + 1)


