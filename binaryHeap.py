# CMSC 122 (C-3L) Week 6 Laboratory Activity
# Joseph Francis Buhayan, Xander Jay Cagang, Michael James Mangaron, Joe Hanna Cantero, Charisse Lorejo, Krystel Mikylla Perez

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2 

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def swap(self, i, j):  # Fixed: changed Swap to swap for consistency
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i] 

    def heapifyUp(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:  
            self.swap(i, self.parent(i))  # Fixed: changed Swap to swap
            i = self.parent(i)

    def heapifyDown(self, i):
        min_index = i               
        left = self.leftChild(i)    
        right = self.rightChild(i)

        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left

        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if i != min_index:
            self.swap(i, min_index)  # Fixed: changed Swap to swap
            self.heapifyDown(min_index)

    def insert(self, value):
        self.heap.append(value)
        self.heapifyUp(len(self.heap) - 1)  

    def delete(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):  # Added missing method
        return len(self.heap)

    def display(self):
        """Display the heap as a tree structure"""
        if not self.heap:
            print("Heap is empty!")
            return
        
        print("\nMin Heap Tree Structure:")
        print("=" * 60)
        
        height = self._calculate_height()
        level = 0
        index = 0
        
        while level <= height:
            nodes_in_level = 2 ** level
            spaces_between = (2 ** (height - level + 1)) - 1
            spaces_side = (2 ** (height - level)) - 1
            
            # Print left spacing
            print(" " * (spaces_side * 3), end="")
            
            # Print nodes for current level
            for i in range(nodes_in_level):
                if index < len(self.heap):
                    print(f"{self.heap[index]:2d}", end="")
                    index += 1
                else:
                    print(" *", end="")
                
                # Print spacing between nodes
                if i < nodes_in_level - 1:
                    print(" " * (spaces_between * 3), end="")
            
            print()
            level += 1
        print("=" * 60)

    def _calculate_height(self):
        """Calculate the height of the heap"""
        n = len(self.heap)
        if n == 0:
            return 0
        height = 0
        while (2 ** height - 1) < n:
            height += 1
        return height - 1

    def __str__(self):
        return str(self.heap)

# Max heap
class MaxHeap:
    def __init__(self, cap):
        self.cap = cap # maximum number of elements
        self.n = 0 # n = the current size
        self.a = [0] * (cap + 1) 
        # ignore 0 so the max heap starts at index 1 for cleaner formulas for the nodes

    def parent(self, i): 
        return i // 2 #formula for the parent node

    def left(self, i):
        return 2 * i # formula for the left child node

    def right(self, i):
        return 2 * i + 1 
        # formula for the right child node (plus 1 cus it's just next to the left sibling)

    # checks leaf nodes using size n
    def isLeaf(self, i): 
        return i > (self.n // 2)

    # swap function
    def swap(self, i, j):
        self.a[i], self.a[j] = self.a[j], self.a[i]

    #fixes the heap from top to bottom
    # every parent node should be greater than its children nodes
    def maxHeapify(self, i):
        if i > self.n: # error handling
            return
            
        largest = i
        left = self.left(i)
        right = self.right(i)
        
        if left <= self.n and self.a[left] > self.a[largest]: # comparison with the left child
            largest = left
            
        if right <= self.n and self.a[right] > self.a[largest]: # comparison with the right child
            largest = right
            
        if largest != i: # swap the parent node with the child node that is greater than it
            self.swap(i, largest)
            self.maxHeapify(largest)
    
    # insertion function
    def insert(self, val):
        # checks if the heap is full
        if self.n >= self.cap:
            print("Heap is full!")
            return
        self.n += 1 # adds the current size number
        self.a[self.n] = val # put the value in the next index
        # switches with the parent node if the new value is greater than it and it reiterates until satisfied
        i = self.n
        while i > 1 and self.a[i] > self.a[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    # return and remove the max value
    def extractMax(self):
        if self.n == 0: # error handling
            return None
        max_val = self.a[1] # the max is always the root
        self.a[1] = self.a[self.n] # switches the max value with the last element
        self.n -= 1 # decreases the size n number
        self.maxHeapify(1) #fix the structure
        return max_val 

    def peek(self):
        return self.a[1] if self.n > 0 else None #returns the current max but does not remove it

    def size(self): 
        return self.n # returns the size number

    # display function
    def display(self):
        """Display the heap as a tree structure"""
        if self.n == 0:
            print("Heap is empty!")
            return
        
        print("\nMax Heap Tree Structure:")
        print("=" * 60)
        
        height = self._calculate_height()
        level = 0
        index = 1
        
        while level <= height:
            nodes_in_level = 2 ** level
            spaces_between = (2 ** (height - level + 1)) - 1
            spaces_side = (2 ** (height - level)) - 1
            
            # Print left spacing
            print(" " * (spaces_side * 3), end="")
            
            # Print nodes for current level
            for i in range(nodes_in_level):
                if index <= self.n:
                    print(f"{self.a[index]:2d}", end="")
                    index += 1
                else:
                    print(" *", end="")
                
                # Print spacing between nodes
                if i < nodes_in_level - 1:
                    print(" " * (spaces_between * 3), end="")
            
            print()
            level += 1
        print("=" * 60)
    
    def _calculate_height(self):
        """Calculate the height of the heap"""
        if self.n == 0:
            return 0
        height = 0
        while (2 ** height - 1) < self.n:
            height += 1
        return height - 1

    def printHeap(self):
        print([self.a[i] for i in range(1, self.n + 1)])


def main():
    def min_heap_menu():
        heap = MinHeap()
        while True:
            print("\n" + "="*50)
            print("MIN HEAP MENU")
            print("="*50)
            print("1. Insert value")
            print("2. Delete minimum")
            print("3. Peek minimum")
            print("4. Display tree structure")
            print("5. Print heap array")
            print("6. Get size")
            print("7. Back to main menu")
            
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                try:
                    value = int(input("Enter value to insert: "))
                    heap.insert(value)
                    print(f"Value {value} inserted successfully!")
                    heap.display()
                except ValueError:
                    print("Please enter a valid integer!")
                    
            elif choice == '2':
                min_val = heap.delete()
                if min_val is not None:
                    print(f"Deleted minimum value: {min_val}")
                    heap.display()
                else:
                    print("Heap is empty!")
                    
            elif choice == '3':
                min_val = heap.peek()
                if min_val is not None:
                    print(f"Minimum value: {min_val}")
                else:
                    print("Heap is empty!")
                    
            elif choice == '4':
                heap.display()
                
            elif choice == '5':
                print("Heap array:", heap)
                
            elif choice == '6':
                print(f"Heap size: {heap.size()}")
                
            elif choice == '7':
                break
                
            else:
                print("Invalid choice! Please enter 1-7")

    def max_heap_menu():
        try:
            cap = int(input("Enter maximum capacity for Max Heap: "))
            if cap <= 0:
                print("Capacity must be positive!")
                return
        except ValueError:
            print("Please enter a valid integer!")
            return
            
        heap = MaxHeap(cap)
        while True:
            print("\n" + "="*50)
            print("MAX HEAP MENU")
            print("="*50)
            print("1. Insert value")
            print("2. Extract maximum")
            print("3. Peek maximum")
            print("4. Display tree structure")
            print("5. Print heap array")
            print("6. Get size")
            print("7. Back to main menu")
            
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                try:
                    value = int(input("Enter value to insert: "))
                    heap.insert(value)
                    heap.display()
                except ValueError:
                    print("Please enter a valid integer!")
                    
            elif choice == '2':
                max_val = heap.extractMax()
                if max_val is not None:
                    print(f"Extracted maximum value: {max_val}")
                    heap.display()
                else:
                    print("Heap is empty!")
                    
            elif choice == '3':
                max_val = heap.peek()  # Now this will work
                if max_val is not None:
                    print(f"Maximum value: {max_val}")
                else:
                    print("Heap is empty!")
                    
            elif choice == '4':
                heap.display()
                
            elif choice == '5':
                heap.printHeap()
                
            elif choice == '6':
                print(f"Heap size: {heap.size()}")  # Now this will work
                
            elif choice == '7':
                break
                
            else:
                print("Invalid choice! Please enter 1-7")

    def run_demo():
        print("\n" + "="*50)
        print("DEMONSTRATION WITH PRE-DEFINED VALUES")
        print("="*50)
        
        print("\nMIN HEAP DEMONSTRATION:")
        heap = MinHeap()
        
        values = [10, 20, 5, 30, 3, 15, 25, 8, 12, 18]
        for val in values:
            print(f"Insert {val}")
            heap.insert(val)
        
        heap.display()
        print("Heap array:", heap)
        
        print("\nDeleting min element:", heap.delete())
        heap.display()

        print("\nMAX HEAP DEMONSTRATION:")
        max_heap = MaxHeap(15)
        max_values = [10, 20, 5, 30, 3, 15, 25, 8, 12, 18]
        for val in max_values:
            print(f"Insert {val}")
            max_heap.insert(val)
        
        max_heap.display()
        print("Heap array:", [max_heap.a[i] for i in range(1, max_heap.n + 1)])

    # Main menu loop
    while True:
        print("\n" + "="*50)
        print("HEAP DATA STRUCTURE DEMONSTRATION")
        print("="*50)
        print("1. Min Heap Operations")
        print("2. Max Heap Operations")
        print("3. Run Demo (Pre-defined values)")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            min_heap_menu()
            
        elif choice == '2':
            max_heap_menu()
            
        elif choice == '3':
            run_demo()
            
        elif choice == '4':
            print("Thank you for using Heap Demonstration!")
            break
            
        else:
            print("Invalid choice! Please enter 1-4")

if __name__ == '__main__':
    main()