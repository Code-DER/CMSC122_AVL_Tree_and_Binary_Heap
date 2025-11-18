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