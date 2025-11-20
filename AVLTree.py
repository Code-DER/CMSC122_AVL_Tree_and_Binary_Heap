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
    # Returns height of the node
    if not node:
        return 0
    return node.height

def getBalance(node):
    # Computes the balance factor of a node
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
    # Performs right rotation on node y
    print("--> Rotate right on node", y.data)
    x = y.left # X becomes the new root of the rotated subtree
    T2 = x.right # T2 is temporarily stored because it moves
    # Rotation
    x.right = y
    y.left = T2
    # Update heights of x and y after rotation
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x

def leftRotate(x):
    # Performs left rotation on node x
    print("--> Rotate left on node", x.data)
    y = x.right # y becomes the new root of the rotated subtree
    T2 = y.left # T2 is temporarily stored because it moves
    # Perform rotation
    y.left = x
    x.right = T2
    # Update heights of x and y after rotation
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y

def insert(node, data):
    if not node:
        return treeNode(data), True
    
    # Insert node in right position just like in BST
    if data < node.data:
        node.left, inserted = insert(node.left, data)
    elif data > node.data:
        node.right, inserted = insert(node.right, data)
    else:
        # Do not insert duplicate value
        return node, False
    
    if not inserted:
        return node, False

    # Update height of current node
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    # Compute for the balance factor
    balance = getBalance(node)

    # Left Left Case (Left Heavy)
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node), True
    
    # Left Right Case (Heavy on left child's right)
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node), True
    
    # Right Right Case (Right Heavy)
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node), True
    
    # Right Left Case (Heavy on right child's left)
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node), True
    
    return node, True

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deletion(node, data):
    if not node:
        return node, False
    
    deleted = False

    if data < node.data:
        node.left, deleted = deletion(node.left, data)
    elif data > node.data:
        node.right, deleted = deletion(node.right, data)
    else:
        deleted = True
        if node.left is None:
            temp = node.right
            node = None
            return temp, True
        elif node.right is None:
            temp = node.left
            node = None
            return temp, True
        
        temp = minValueNode(node.right)
        node.data = temp.data
        node.right, _ = deletion(node.right, temp.data)
    
    if not deleted:
        return node, False
    
    if node is None:
        return node, False
    
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Balancing the tree
    # Left left
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node), True
    
    # Left right
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node), True
    
    # Right right
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node), True
    
    # Right left
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node), True
    
    return node, True

# Breadth First Search Traversal Function
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

# Pre Order Traversal Function
def preOrderTraversal(node):
    if node is None:
        return []
    return [node.data] + preOrderTraversal(node.left) + preOrderTraversal(node.right)

# In Order Traversal Function
def inOrderTraversal(node):
    if node is None:
        return []
    return inOrderTraversal(node.left) + [node.data] + inOrderTraversal(node.right)

# Post Order Traversal function
def postOrderTraversal(node):
    if node is None:
        return []
    return postOrderTraversal(node.left) + postOrderTraversal(node.right) + [node.data]

# Function for printing tree
def printTree(node, level=0):
    if node is not None:
        printTree(node.right, level + 1)
        print(' ' * 5 * level + '->', node.data)
        printTree(node.left, level + 1)

# Main menu
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
            root, deleted = deletion(root, node)
            if deleted:
                print(f"--> Deleted {node} from AVL tree.")
            else:
                print(f"--> Node {node} not found in the AVL tree.")
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