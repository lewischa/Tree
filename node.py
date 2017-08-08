class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def __str__(self):
        return "Data: {data}; Left: {left}; Right: {right}".format(data=self._data, left=self._left, right=self._right)

    def data(self, new=None):
        if new is None:
            return self._data
        else:
            self._data = new

    def left(self, next=None):
        if next is None:
            return self._left
        else:
            self._left = next

    def right(self, next=None):
        if next is None:
            return self._right
        else:
            self._right = next
