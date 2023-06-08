class Node:
    def __init__(self,x,y, next=None):
        self.__x = x
        self.__y = y
        self.__next = next

    def get_data(self):
        return (self.__x,self.__y)
    def get_next(self):
        return self.__next
    def set_data(self,x,y):
        self.__x = x
        self.__y = y
    def set_next(self,next):
        self.__next = next


class LinkedList:
    def __init__(self, head=None):
        self.__head = head
    def get_head(self):
        return self.__head
    def is_empty(self):
        return self.__head == None
    def add(self, new_head):
        new_head.set_next(self.__head)
        self.__head = new_head
    def pop_lest(self):

