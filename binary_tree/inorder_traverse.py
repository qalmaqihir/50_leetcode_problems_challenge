class Node:
    def __int__(self,value):
        self.left=None
        self.right=None
        self.data=value


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data)
        inorder(node.right)


root=Node(5)
root.left=Node(4)
root.right=Node(8)
inorder(root)