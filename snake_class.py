class Vertebra:
    """
    A vertebra is a vertebra in a snake.
    or doble side linked object.
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
        return self.next


    def dis_connect(self):
        """
        Severs the vertebra from the previous vertebra
        :return: None
        """
        self.prev = None
        return self





class Snake:
    """An object that holds the ends of a verbatra chain."""
    def __init__(self):
        """
         A constructor for a snake object.
        """
        self.__head = None
        self.__tail = None
        self.__length = 3
        self.grouth = 0
        self.score = 0


    def __str__(self):
        """
        Prints a sequence of tuples containing the positions within the snake's vertebra
        :return: str(string of loc tuple)
        """
        current = self.get_head()
        loc_string = ''
        while current != None:
            loc_string += str(current.get_loc()) +','
            current = current.prev
        return loc_string[:-1]


    def __len__(self):
        """Returns the length of the snake"""
        i = 0
        current = self.__head
        while current != None:
            i += 1
            current = current.prev
        return i




    def snake_starter(self, row: int, col: int):
        '''
        get head loc and conect 2 Vertebra to it.
        '''

        self.__tail = Vertebra((row, col - 2))
        curent = self.__tail
        for i in range(-1,1):
            curent.creat_next((row, col + i))
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
        """
        A recursive function runs from head to tail and returns all positions
        :param cor: the loc of the object
        :param index:
        :return: loc + nex.loc .... tail.loc
        """
        if index >= (self.__len__()):
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
        """
        Returns the position of the snake's head
        """
        return self.__head.get_loc()
    def get_tail_loc(self):
        '''
        Returns the position of the snake's tail
        '''
        return self.__tail.get_loc()
    def pop_lest(self):
        '''
        drop the lest vertebra of the snake
        :return: None
        '''
        self.__tail = self.__tail.next
        self.__tail.dis_connect()


    def move_snake(self, loc, apple):
        """
        Performs Snake's Head Step.
        By adding a verbata in front of the head.
        Update the increment value if an apple has been updated.
        If increment value == 0.
        will remove the last verbata.
        :param loc: the new loc of the head
        :param apple: bool. if apple got eaten
        """
        new_vertebra = self.__head.creat_next(loc)
        self.__head = new_vertebra
        if self.grouth > 0:
            self.__length += 1
            self.grouth -= 1
        else:
            self.pop_lest()
        if apple == True:
            self.grouth += 3
            self.snake_score()


    def snake_score(self):

        self.score += int((len(self) ** 0.5) // 1)


    def cut_snake(self,loc):
        """
        Gets a LOC value from the snake and assigns it to the tail.
        and disconnects the varbatas
        :param loc: the loc of the new tail
        """
        i = 0
        corrent = self.__head
        while corrent.prev.get_loc() != loc:
            corrent= corrent.prev
            i += 1
        corrent.dis_connect()
        self.__tail = corrent
        self.__length = i


    def decapitation(self):
        '''
        this code cut the snake head
        '''
        self.__head = self.__head.prev
        self.__head.next = None
