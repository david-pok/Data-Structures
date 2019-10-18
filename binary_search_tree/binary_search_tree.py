import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
        # important <<<<<<<<<<<<<<<<<<<<<<<<
    def insert(self, value):
        if value < self.value:
            # go left
            if not self.left:
                # create a tree at the spot
                # because each node is a tree in itself
                self.left = BinarySearchTree(value)
            else:
                # if there is something there
                # we recursively call to start process over from start
                # if there's a left, we call again, and go left again, call again, go left again as necessary
                self.left.insert(value)
        else:
            # go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
                # important <<<<<<<<<<<<<<<<<<<<<<<<<<<
    def contains(self, target):
        # if current node is our target, return true
        if self.value == target:
            return True
        # if target is less than value, go left
        if target < self.value:
            # if there is no left, return false
            # if there is no left, there are no targets smaller than current node
            if not self.left:
                return False
            else:
                # if there is left, recursively call to keep going until we find
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # highest numbers will always go to the right, so we need to look to the right
        # if there is no right, return the current node
        # if there's no right then the current node is the largest
        # if there is a right, then we call get max recursively on the right so that we can keep going right
        # over and over until we reach the end
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)

        while q.size > 0:
            deq = q.dequeue()
            print(deq.value)
            if deq.left:
                q.enqueue(deq.left)
            if deq.right:
                q.enqueue(deq.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.size > 0:
            popped = stack.pop()
            print(popped.value)
            if popped.left:
                stack.push(popped.left)
            if popped.right:
                stack.push(popped.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
