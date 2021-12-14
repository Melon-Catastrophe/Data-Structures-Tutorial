import time
import random
from collections import deque

class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root == None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left == None:
                node.left = BST.Node(data)  # We have to call a Node object so that .left and .right parameters exist.
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right == None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)
        elif data == node.data:
            # Do nothing; we do not want duplicates.
            pass
    

    '''
    "__contains__()" is used in keyword 'in'. Example: if 5 in bst: ...
    '''
    def __contains__(self, data):
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        # Base Case: Node is empty or node matches data.
        if node is not None:
            if data == node.data:
                return True
            elif data < node.data:
                return self._contains(data, node.left)
            elif data > node.data:
                return self._contains(data, node.right)
        else:
            assert node is None, "Only runs when node is None; _contains()"
            return False

    '''
    '__iter__' prints all elements in the tree.
    '''
    def __iter__(self):
    
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
       
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
        yield from self._traverse_backward(self.root)  # Start at the root
    def _traverse_backward(self, node):
        # If node is full...
        if node is not None:
            # yield from right first,...
            yield from self._traverse_backward(node.right)
            yield node.data # Present data (yield),...
            yield from self._traverse_backward(node.left)
            # then yield from the left tree.

            # This algorithm presents the right-most branch, then proceeds to left branches.

'''
Solution to Problem 2 Below
'''
# Comments are only given on the timing_lists() function, since the four
# functions below are nearly identical.
def timing_lists(num_times):
    timed_list = []
    # Adding random integers in the range of num_times to timed_list.
    for i in range(num_times):
        timed_list.append(random.randint(1, num_times))
    
    # Determining if random integers are located inside of timed_list.
    # We use random integers to give us a good look at a possible actual
    # use case scenario.
    start_time = time.time()
    for i in range(num_times):
        if random.randint(1, num_times) in timed_list:
            pass
    end_time = time.time()

    # Returning the time in seconds it took to execute the above block of code.
    # We start the time only after all data is inserted into the list, since
    # we are gauging the performance of accessing variables in collections,
    # not the performance of adding a variable to collections.
    return end_time - start_time


def timing_sets(num_times):
    timed_set = set()
    for i in range(num_times):
        timed_set.add(random.randint(1, num_times))

    start_time = time.time()
    for i in range(num_times):
        if random.randint(1, num_times) in timed_set:
            pass
    end_time = time.time()
    
    return end_time - start_time


def timing_queues(num_times):
    timed_q = deque()
    for i in range(num_times):
        timed_q.append(random.randint(1, num_times))

    start_time = time.time()
    for i in range(num_times):
        if random.randint(1, num_times) in timed_q:
            pass
    end_time = time.time()
    
    return end_time - start_time


def timing_trees(num_times):
    timed_tree = BST()
    for i in range(num_times):
        timed_tree.insert(random.randint(1, num_times))

    start_time = time.time()
    for i in range(num_times):
        if random.randint(1, num_times) in timed_tree:
            pass
    end_time = time.time()

    return end_time - start_time

'''
Testing the above code to look for the execution times below.
'''

execution_list = []
execution_list.append(timing_lists(1000))
execution_list.append(timing_lists(5000))
execution_list.append(timing_lists(10000))
execution_list.append(timing_lists(15000))
print("Execution Times for List:", execution_list)
# My list execution times were [0.0069806575775146484, 0.16558313369750977, 0.6781594753265381, 1.5299067497253418].

execution_set = []
execution_set.append(timing_sets(1000))
execution_set.append(timing_sets(5000))
execution_set.append(timing_sets(10000))
execution_set.append(timing_sets(15000))
print("Execution Times for Set:", execution_set)
# My set execution times were [0.0009970664978027344, 0.00501561164855957, 0.009966850280761719, 0.01396322250366211].

execution_queue = []
execution_queue.append(timing_queues(1000))
execution_queue.append(timing_queues(5000))
execution_queue.append(timing_queues(10000))
execution_queue.append(timing_queues(15000))
print("Execution Times for Queue:", execution_queue)
# My queue execution times were [0.008977413177490234, 0.1825113296508789, 0.7350594997406006, 1.6047465801239014].

execution_tree = []
execution_tree.append(timing_trees(1000))
execution_tree.append(timing_trees(5000))
execution_tree.append(timing_trees(10000))
execution_tree.append(timing_trees(15000))
print("Execution Times for Tree:", execution_tree)
# My tree execution times were [0.004019021987915039, 0.021910429000854492, 0.04690718650817871, 0.07579731941223145].

'''
In comparing the four different collection types above, one thing stands out:
sets are much faster than all of the rest in terms of efficiency. However, 
accessing data in trees was only a few times slower. It is to be expected when compared
to a set (especially since our trees are likely unsorted), but trees have one advantage
over sets: they are sorted. If one needs a sorted set, then a tree is a good option to 
have.
'''