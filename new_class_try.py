class vertebra:

    def __init__(self,x,y, next=None, prev= None):
        self.__x = x
        self.__y = y
        self.__next = next
        self.prev = prev

    def get_loc(self):
        return (self.__x,self.__y)
    def get_next(self):
        return self.__next
    def set_loc(self,x,y):
        self.__x = x
        self.__y = y
    def set_next(self,next):
        self.__next = next


class snake:
    ITEM_NOT_FOUND = -1
    def __init__(self, head=None):
        self.__head = None
        self.__tail = None
        self.__length = 0
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
        loc  = self.__tail.get_loc()

        self.__tail = self.__tail.prev
        if self.__tail is None:  # list is now empty
            self.__head = None
        else:  # disconnect old tail
            self.__tail.next.prev = None
        self.__tail.next = None
        self.__length -= 1
        return loc
    def move_snake_left(self, apple = False):
        new_vertebra = vertebra(x = self.__head.get_loc()[0]-1,y=self.__head.get_loc()[1])
        self.add_first(new_vertebra)
        if apple==True:
            self.__length +=1
        else:
            self.pop_lest()

    def move_snake_right(self, apple = False):
        new_vertebra = vertebra(x=self.__head.get_loc()[0] + 1, y=self.__head.get_loc()[1])
        self.add_first(new_vertebra)
        if apple == True:
            self.__length += 1
        else:
            self.pop_lest()
    def move_snake_up(self, apple = False):
        new_vertebra = vertebra(x=self.__head.get_loc()[0], y=self.__head.get_loc()[1]+1)
        self.add_first(new_vertebra)
        if apple == True:
            self.__length += 1
        else:
            self.pop_lest()
    def move_snake_down(self, apple = False):
        new_vertebra = vertebra(x=self.__head.get_loc()[0], y=self.__head.get_loc()[1]-1)
        self.add_first(new_vertebra)
        if apple == True:
            self.__length += 1
        else:
            self.pop_lest()
    def __len__(self):
        current = self.__head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count
    def collision(self, loc):
        if self.collision_helper(self.__head, loc, 0) == -1:
            return False
        else: return True

    def collision_helper(self, cur, loc, index):
        if index >= self.__len__():
            return -1

        if cur.get_loc() == loc:
            return index
        return self.collision_helper(cur.get_next(), loc,index + 1)


