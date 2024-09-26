class newNode:
    def __init__(self, data):
        self.key = data
        self.right = None
        self.left = None


def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.key, end=' ')
    inorder(temp.right)


def insert(temp, key):
	q = []
	q.append(temp)
	while (len(q)):
		temp = q[0]
		q.pop(0)
		if ( not temp.left ):
			temp.left = newNode(key)
			break
		else:
			q.append(temp.left)


		if (not temp.right):
			temp.right = newNode(key)
			break
		else:
			q.append(temp.right)



if __name__ == '__main__':
	root = newNode(10)
	root.left = newNode(11)
	root.right = newNode(12)
	root.left.left = newNode(13)
	root.left.right = newNode(14)
	inorder(root)

	insert(root, 15)
	print()
	inorder(root)

