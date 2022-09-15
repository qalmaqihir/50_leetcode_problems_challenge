def post_order_traverse(tree):
    if tree is not None:
        post_order_traverse(tree.left)
        post_order_traverse(tree.right)
        print(tree.data)