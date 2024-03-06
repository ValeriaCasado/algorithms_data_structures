"""

A linked list can be defined as a doubly-celled list
composed of a value and a pointer.
"""
class LinkedList:

    # Making a Cell class and make the pointer
    # Able to take a Cell instance without defining it
    # But this wouldn't work with strictly typed languages
    class Cell:
        def __init__(self, value, pointer):
            self.value = value
            self.pointer = pointer


    def __init__(self):
        self.head = None

    def empty_list(self):
        # Gives you the empty list
        return []

    def make_list(self, value, array):
        # Puts an element at the top of an existing list.
        # MakeList(3, MakeList(1, MakeList(4, MakeList(2, MakeList(5, EmptyList))))).
        pass

    def first(self):
        # Gets first element
        pass
    
        
    def rest(self):
        # Everything that is not first
        pass

    def is_empty(self):
        pass

    def replace_first(self, value, array):
        pass

    def replace_rest(self, value, array):
        pass

