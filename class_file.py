
class Vertebra:
    """
    An object that contains information about the presence of the next vertebra in the snake.
    The Vertebra can be formed from the last link.
    """
    def __init__(self, num, loc, next = None):
        """
        :param num: The number of the link in the chain.
        :param orientation:The direction the chain continues.
        0-3 so that within modulo 4 turning left is always minus 1 and turning right is plus 1.
        regardless of the absolute direction.
        :param next: the nex vertebra
        """
        self.num = num
        self.loc = loc
        if next != None:
            self.next = Vertebra(next)
        else:
            self.next = None


    def add_vertebra_link(self):
        if self.next == None:
            self.next = Vertebra(self.num+1, self.loc)
        else:
            self.next.add_vertebra_link()


    def chain_lenth(self):
        if self.next == None:
            return self.num
        else:
            return self.next.chain_lnth()

    def pass_to_next(self,):



class Snake:

    def __int__(self,height,width):
        self.head = SnakeHead(tuple(height//2 ,width//2))


class SnakeHead:
    """
    The head of the serpent holds the first link.
    All actions from the game and to the vertebras will be performed on it.
    """
    def __init__(self, loc: tuple):
        self.__loc = loc
        self.body = Vertebra(0, loc,(1, (loc[0]-1,loc[1]),(2 ,(loc[0]-2, loc[1]))))



class Apple:
    pass
class Wall:
    pass

