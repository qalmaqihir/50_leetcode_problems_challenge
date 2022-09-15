class Node:
    def __int__(self, value):
        self.data = value
        self.left = None
        self.right = None


root = Node(5)
# '''
#     5
#    /  \
#  None  None
# '''

root.left = Node()
root.data(4)

root.right = Node(7)
