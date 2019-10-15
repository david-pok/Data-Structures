from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        self.storage.pop(-1)

    def len(self):
        return self.size
