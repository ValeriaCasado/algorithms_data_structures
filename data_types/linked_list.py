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

    
    def make_list(self):
        self.head = None
    
    def get_list(self):
        next_element = self.head
        complete_list = []
        while(next_element):
            complete_list.append(next_element)
            next_element = next_element.pointer
        return complete_list
    
    def first(self):
        return self.head()

    def rest(self):
        pass

    def tail(self):
        next_element = self.head
        while(next_element):
            next_element = next_element.pointer
        return next_element

    def is_empty(self):
        return self.head != None


    def replace_value(self, original_value, dst_value):
        counter = 0
    
    def replace_at_p

        

