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