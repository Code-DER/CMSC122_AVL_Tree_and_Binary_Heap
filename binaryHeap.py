class MinHeap:
    def __init__(self):
        # Declaration of empty min heap
        self.heap = []

    def parent(self, i):
        # Returns the index of the parent of the node at index i.
        return (i - 1) // 2 

    def leftChild(self, i):
        # Returns the index of the left child of the node at index i.
        return 2 * i + 1

    def rightChild(self, i):
        # Returns the index of the right child of the node at index i.
        return 2 * i + 2

    def Swap(self, i, j):
        # Swaps the elements at indices i and j in the heap.
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i] 

    def heapifyUp(self, i):
        # Moves the node at index i up the heap to its correct position.
        # This is used after insertion.
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:  
            self.Swap(i, self.parent(i))                            
            i = self.parent(i)

    def heapifyDown(self, i):
        # Moves the node at index i down the heap to its correct position.
        # This is used after deletion.
        min_index = i               
        left = self.leftChild(i)    
        right = self.rightChild(i)

        # Check if left child is smaller than the current node
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left

        # Check if right child is smaller than the current smallest
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        # If the smallest is not the current node, Swap and continue heapifying down
        if i != min_index:
            self.Swap(i, min_index)
            self.heapifyDown(min_index)

    def insert(self, value):
        # Inserts a new value into the heap.
        self.heap.append(value)
        self.heapifyUp(len(self.heap) - 1)  

    def delete(self):
        # Deletes and returns the minimum element from the heap.
        # The minimum element is always at the root.
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        # Move the last element to the root
        self.heap[0] = self.heap.pop()

        # Restore the heap property
        self.heapifyDown(0)

        return root

    def peek(self):
        # Returns the minimum element without removing it.
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)

# Max heap
class MaxHeap:
    # constructor
    def __init__(self, cap):
        self.cap = cap # the max number of elements allowed
        self.n = 0 # the current size of the heap
        self.a = [0] * (cap + 1) # ignore index 0 so the heap starts at index 1 for cleaner formulas for the nodes

    #formula for the parent node
    def parent(self, i):
        return i // 2 

    #formula for the left child node
    def left(self, i):
        return 2 * i

    # formula for the right child node (bc it's right next to the left child so just add 1)
    def right(self, i):
        return 2 * i + 1

    # checks for leaf nodes using n
    def isLeaf(self, i):
        return i > (self.n // 2) and i <= self.n

    #swap function
    def swap(self, i, j):
        self.a[i], self.a[j] = self.a[j], self.a[i]

    # fix the heap from top to bottom
    # every parent node should be greater than its children nodes
    def maxHeapify(self, i):
        if not self.isLeaf(i):
            largest = i
            if self.left(i) <= self.n and self.a[i] < self.a[self.left(i)]: # comparison with left child
                largest = self.left(i)
            if self.right(i) <= self.n and self.a[largest] < self.a[self.right(i)]: # comparison with right child
                largest = self.right(i)
            if largest != i: # swap if either of the children is bigger
                self.swap(i, largest)
                self.maxHeapify(largest)

    # insert a value
    def insert(self, val):
        if self.n >= self.cap: # checks if heap is full
            print("Heap is full!")
            return
        self.n += 1 # places the new value at n + 1
        self.a[self.n] = val
        i = self.n
        while i > 1 and self.a[i] > self.a[self.parent(i)]: # switches with parent if the inserted value is bigger, loops until satisfied
            self.swap(i, self.parent(i))
            i = self.parent(i)

    # remove and return the max 
    def extractMax(self):
        if self.n == 0:
            return None
        max_val = self.a[1] # the max is always the root
        self.a[1] = self.a[self.n] # swaps the max with the last element
        self.n -= 1 # decrease size
        self.maxHeapify(1) #fix the max heap after the swap
        return max_val 

    # print
    def printHeap(self):
        print([self.a[i] for i in range(1, self.n + 1)])

if __name__ == '__main__':
    heap = MinHeap()
    print("Insert 10")
    heap.insert(10)

    print("Insert 20")
    heap.insert(20)

    print("Insert 5")
    heap.insert(5)

    print("Insert 30")
    heap.insert(30)

    print("Insert 3")
    heap.insert(3)

    print("Min Heap:", heap)

    print("Peek min element:", heap.peek())


    print("Deleted min element:", heap.delete())
    print("Min Heap after deletion:", heap)

    print("Deleted min element:", heap.delete())
    print("Min Heap after deletion:", heap)

    # menu driven program
    # print("Choose Heap Type:")
    # print("1. Min Heap")
    # print("2. Max Heap")

    # choice = input("Enter choice (1/2): ")

    # if choice == '1':
    #     heap = MinHeap()
    #     while True:
    #         print("\nMin Heap Menu:")
    #         print("1. Insert")
    #         print("2. Delete Min")
    #         print("3. Peek")
    #         print("4. Print")
    #         print("5. Exit")
    #         c = input("Choice: ")

    #         if c == '1':
    #             heap.insert(int(input("Enter value: ")))
    #         elif c == '2':
    #             print("Deleted:", heap.delete())
    #         elif c == '3':
    #             print("Min:", heap.peek())
    #         elif c == '4':
    #             print("Heap:", heap)
    #         elif c == '5':
    #             break

    # elif choice == '2':
    #     cap = int(input("Enter Max Heap capacity: "))
    #     heap = MaxHeap(cap)

    #     while True:
    #         print("\nMax Heap Menu:")
    #         print("1. Insert")
    #         print("2. Extract Max")
    #         print("3. Print")
    #         print("4. Exit")
    #         c = input("Choice: ")

    #         if c == '1':
    #             heap.insert(int(input("Enter value: ")))
    #         elif c == '2':
    #             print("Max:", heap.extractMax())
    #         elif c == '3':
    #             heap.printHeap()
    #         elif c == '4':
    #             break