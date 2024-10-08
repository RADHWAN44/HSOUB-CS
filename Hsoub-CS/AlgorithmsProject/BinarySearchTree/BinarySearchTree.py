class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key



def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def search(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right, key)

    return search(root.left, key)


def mainValueNode(node):
    current = node

    while(current.left is not None):
        current = current.left

    return current




def delete_node(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)

    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = mainValueNode(root.right)

        root.val = temp.val

        root.right = delete_node(root.right, temp.val)



    return root






root = Node(50)

insert(root,Node(60))
insert(root,Node(70))
insert(root,Node(30))
insert(root,Node(40))
insert(root,Node(20))
insert(root,Node(10))


r = delete_node(root, 20)


inorder(root)






