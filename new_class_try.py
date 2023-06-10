class Vertebra:
    """
    A vertebra is a vertebra in a snake.
    containing information about its location(LOC) on its parent (PERV) and on its son (NEXT).
    """
    def __init__(self, loc: tuple, prev= None):
        """
        A constructor for a Vertebra object.
        :param loc: tuple, contain the location of the vertebra.
        :param prev: if creat fron another vertebra, contain her ID.
        """
        self.__loc = loc
        self.prev = prev
        self.next = None


    def get_loc(self):
        """
        Returns the loc of the vertebra.
        :return: tupel(loc).
        """
        return (self.__loc)


    def creat_next(self,new_loc):
        """
        Produces a new vertebra and produces father-son connectivity between the vertebrae.
        :param new_loc: the loc of the new vertebra
        :return: self.next
        """
        self.next = Vertebra(new_loc, self)
        #print("creat=", self.next.get_loc()) #!!
        return self.next


    def dis_connect(self):
        """
        Severs the vertebra from the previous vertebra
        :return: None
        """
        self.prev = None
        return self





class Snake:

    ITEM_NOT_FOUND = -1
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 3
        self.grouth = 0

    def __str__(self):
        current = self.get_head()
        loc_string = ''
        while current != None:
            loc_string += str(current.get_loc()) +','
            current = current.prev
        return loc_string[:-1]



    def snake_starter(self, row: int, col: int):
        '''
        get head loc and conect 2 Vertebra to it.
        '''

        self.__tail = Vertebra((row-2,col))
        curent = self.__tail
        for i in range(1,-1,-1):
            curent.creat_next((row-i,col))
            curent = curent.next
        self.__head = curent

    def get_locs(self):
        """
        :return: list of all the lock list
        """
        global loc_list
        loc_list = []
        index=0
        self.get_locs_helper(self.__head,0)
        return loc_list

    def get_locs_helper(self,cor,index):
        if index >= self.__len__():
            return None
        if cor == None: return None
        loc_list.append(cor.get_loc())

        return self.get_locs_helper(cor.prev,index+1)

    def get_head(self):
        """
        check if head is actual head and send it
        :return: head
        """
        if self.__head.next == None:
            return self.__head
        self.__head = self.__head.next
        return self.get_head()

    def get_head_loc(self):
        return self.__head.get_loc()


    def pop_lest(self):
        '''
        drop the lest vertebra of the snake
        :return: None
        '''
        self.__tail = self.__tail.next
        self.__tail.dis_connect()


    def move_snake(self, loc, apple):
        new_vertebra = self.__head.creat_next(loc)
        self.__head = new_vertebra
        if apple == True:
            self.grouth += 3
        if self.grouth > 0:
            self.__length += 1
            self.grouth -= 1
        else:
            self.pop_lest()


    def __len__(self):
        return self.__length


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
        if cur == None: return -1
        if cur.get_loc() == loc:
            return index
        return self.collision_helper(cur.next, loc,index + 1)

    def cut_snake(self,loc):
        i = 1
        corrent = self.__head
        while corrent.prev.get_loc() != loc:
            corrent= corrent.prev
            i += 1
        corrent.dis_connect()
        self.__tail = corrent
        self.__length = i


"""
!
a = Snake()
a.snake_starter(5,5)
print(a)
print(a.get_head().get_loc())
a.move_snake((6,5))
print(a)

"""