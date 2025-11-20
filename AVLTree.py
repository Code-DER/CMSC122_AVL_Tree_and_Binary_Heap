# CMSC 122 (C-3L) Week 6 Laboratory Activity
# Joseph Francis Buhayan, Xander Jay Cagang, Michael James Mangaron, Joe Hanna Cantero, Charisse Lorejo, Krystel Mikylla Perez

from collections import deque

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
    print("--> Rotate right on node", y.data)
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x

def leftRotate(x):
    print("--> Rotate left on node", x.data)
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y

def insert(node, data):
    if not node:
        return treeNode(data), True
    
    if data < node.data:
        node.left, inserted = insert(node.left, data)
    elif data > node.data:
        node.right, inserted = insert(node.right, data)
    else:
        return node, False
    
    if not inserted:
        return node, False

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
    
    return node, True

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deletion(node, data):
    if not node:
        return node
    if data < node.data:
        node.left = deletion(node.left, data)
    elif data > node.data:
        node.right = deletion(node.right, data)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        
        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = deletion(node.right, temp.data)
    
    if node is None:
        return node
    
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Balancing the tree
    # Left left
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)
    
    # Left right
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    
    # Right right
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)
    
    # Right left
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    return node

def breadthFirstSearch(node):
    if node is None:
        return []
    
    result = []
    queue = deque([node])
    while queue:
        node = queue.popleft()
        # print(node.data, end=" ")
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def preOrderTraversal(node):
    if node is None:
        return []
    return [node.data] + preOrderTraversal(node.left) + preOrderTraversal(node.right)
    # print(node.data, end=" ")
    # preOrderTraversal(node.left)
    # preOrderTraversal(node.right)

def inOrderTraversal(node):
    if node is None:
        return []
    return inOrderTraversal(node.left) + [node.data] + inOrderTraversal(node.right)
    # inOrderTraversal(node.left)
    # print(node.data, end=" ")
    # inOrderTraversal(node.right)

def postOrderTraversal(node):
    if node is None:
        return []
    return postOrderTraversal(node.left) + postOrderTraversal(node.right) + [node.data]
    # postOrderTraversal(node.left)
    # postOrderTraversal(node.right)
    # print(node.data, end=" ")

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
            root, successful = insert(root, node)
            if successful:
                print(f"--> Inserted {node} into AVL tree.")
            else:
                print(f"--> Node {node} already exists in the AVL tree.")
            print("\n--> AVL Tree:")
            printTree(root)
        elif choice == '3':
            node = (input("--> Enter value to delete: "))
            root = deletion(root, node)
            print(f"--> Deleted {node} from AVL tree.")
            printTree(root)
        elif choice == '4':
            print("--> Pre-order Traversal:")
            # preOrderTraversal(root)
            print(*preOrderTraversal(root))
            print("\n--> AVL Tree:")
            printTree(root)
        elif choice == '5':
            print("--> In-order Traversal:")
            # inOrderTraversal(root)
            print(*inOrderTraversal(root))
            print("\n--> AVL Tree:")
            printTree(root)
        elif choice == '6':
            print("--> Post-order Traversal:")
            # postOrderTraversal(root)
            print(*postOrderTraversal(root))
            print("\n--> AVL Tree:")
            printTree(root)
        elif choice == '7':
            print("--> Breadth First Search Traversal:")
            # breadthFirstSearch(root)
            print(*breadthFirstSearch(root))
            print("\n--> AVL Tree:")
            printTree(root)
        elif choice == '8':
            print("--> Exiting the program... Byerzzz!!!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    root = None

    print("================================")
    print("Welcome to our AVL Tree Program!")
    print("================================")

    mainMenu(root)

if __name__ == "__main__":
    main()