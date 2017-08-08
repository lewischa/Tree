from node import Node

class Tree(object):
    def __init__(self, root=None):
        self._root = root

    def _found(self, value, root):
        if root is None:
            return False
        if root.data() == value:
            return True
        if root.value() > value:
            return _found(value, root.left())
        else:
            return _found(value, root.right())

    def found(self, value):
        return _found(value, self._root)

    def insert(self, value):
        self._root = _insert(value, self._root)
    
    def _insert(self, value, root):
        if root is None:
            root = Node(value)
            return root
        elif root.value() > value:
            root.left(insert
