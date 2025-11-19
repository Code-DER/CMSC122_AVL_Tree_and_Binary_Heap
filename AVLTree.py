class treeNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    print("Rotate right on node,", y.data)
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x

def leftRotate(x):
    print("Rotate left on node,", x.data)
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y

def insert(node, data):
    if not node:
        return treeNode(data)
    
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)

    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)
    
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)
    
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    return node

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=" ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=" ")
    inOrderTraversal(node.right)

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=" ")

def printTree(node, level=0):
    if node is not None:
        printTree(node.right, level + 1)
        print(' ' * 5 * level + '->', node.data)
        printTree(node.left, level + 1)


def mainMenu(root):
    while True:
        print("\n==== Main Menu ====")
        print("1. Look at AVL Tree")
        print("2. Insert a node")
        print("3. Delete a node")
        print("4. Pre-order Traversal")
        print("5. In-order Traversal")
        print("6. Post-order Traversal")
        print("7. Breadth First Search Traversal")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            print("\n--> AVL Tree:")
            printTree(root)
        elif choice == '2':
            node = input("--> Enter value to insert: ")
            root = insert(root, node)
            print(f"--> Inserted {node} into AVL tree.")
        elif choice == '3':
            node = int(input("--> Enter value to delete: "))
            print("Deleted")
        elif choice == '4':
            print("--> Pre-order Traversal:")
            preOrderTraversal(root)
        elif choice == '5':
            print("--> In-order Traversal:")
            inOrderTraversal(root)
        elif choice == '6':
            print("--> Post-order Traversal:")
            postOrderTraversal(root)
        elif choice == '7':
            print("--> Breadth First Search Traversal:")
        elif choice == '8':
            print("--> Exiting the program... Byerzzz!!!")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    root = None
    # values = [10, 20, 30, 40, 50, 67]

    # for value in values:
    #     root = insert(root, value)

    print("================================")
    print("Welcome to our AVL Tree Program!")
    print("================================")

    mainMenu(root)

if __name__ == "__main__":
    main()



