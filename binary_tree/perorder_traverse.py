def pre_order_traverse(tree):
    if tree is not None:
        print(tree.left)
        pre_order_traverse(tree.left)
        print(tree.right)
        pre_order_traverse(tree.right)
