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
    def __init__(self, head=None):
        self.__head = self.__tail = None
        self.__length = 0

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


    def get_head(self):
        return self.__head
    def is_empty(self):
        return self.__head == None

    def pop_lest(self):

