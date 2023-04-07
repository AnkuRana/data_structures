class Heap:
    def __init__(self):
        pass
    
    def build_heap_max(self, array):
        arr_size = len(array)
        for i in range((arr_size//2)-1,-1, -1):
            # print(i)
            self.max_heapify(array,i, arr_size)
        return array
    
    def build_heap_min(self, array):
        arr_size = len(array)
        for i in range((arr_size//2)-1,-1, -1):
            # print(i)
            self.min_heapify(array,i, arr_size)
        
    def max_heapify(self, array, i, array_size):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < array_size and array[i] < array[l]:
            largest = l
        else:
            largest = i
        if r < array_size and array[largest] < array[r]:
            largest = r
        if largest != i:
            self.swap(array, i , largest)
            self.max_heapify(array, largest, array_size)
    
    def min_heapify(self, array, i, arr_size):
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        if leftChild < len(array) and array[leftChild] < array[i]:
            smallest = leftChild
        else:
            smallest = i
        if rightChild < len(array) and array[rightChild] < array[smallest]:
            smallest = rightChild
        if smallest != i:
            self.swap(array, i , smallest)
            self.min_heapify(array, smallest, arr_size)
    
    def extract_max_or_pop(self, array):
        array_size = len(array)
        if array_size < 1:
            return "Heap is empty."
        max = array[0]
        array[0] = array[array_size-1]
        array_size = array_size - 1
        self.max_heapify(array, 0, array_size)
        return max
    
    def insert_key_max_heap(self, array, val):
        arr_size = len(array)
        # print(arr_size)
        # as we need to add value , increasing size by 1
        # New element needs to be added to the end
        array.append(val)
        # self.build_heap_max(array) #this also works
        arr_size += 1
        inserted_index = arr_size - 1
        # parent = (inserted_index-1)//2
        while inserted_index > 0 and array[(inserted_index-1)//2] < array[inserted_index]:
            self.swap(array, (inserted_index-1)//2, inserted_index)
            inserted_index = (inserted_index-1)//2
        return array
    
    def increase_key_max_heap(self, array, i, new_value): #using max heap
        if array[i] > new_value:
            print("New value is small then current value.")
            return
        array[i] = new_value
        while i > 0 and self.getParentIndex(i) < array[i]:
            self.swap(array, self.getParentIndex(i), i)
            i = self.getParentIndex(i)
        return array
    
    def decrease_key_max_heap(self, array, i, new_value): #using max heap
        if array[i] < new_value:
            print("current is already smaller than new value.")
        array[i] = new_value
        self.max_heapify(array, i, len(array))
    
    def heapSort_max_heap(self, array):
        self.build_heap_max(array)
        array_size = len(array)
        for i in range( array_size - 1, 0, -1):
            # print(i)
            self.swap(array, i, 0)
            self.max_heapify(array, 0, i)
                 
    def getParentIndex(self, node_index):
        return (node_index-1)//2
    
    def swap(self, array, first, second):
        # print(f"first: {first}")
        # print(f"second: {second} ")
        temp = array[first]
        array[first] = array[second]
        array[second] = temp
        

if __name__ == "__main__":
     array = [1, 9, 6, 7, 4, 8, 6 , 5, 3, 2, 10]
    #  arr = [9, 6, 7, 4, 8, 6, 5, 3, 2, 1]
     hp = Heap()
    #  print("Before Build Heap")
    # #  print(array)
    #  print(array)
    # #  hp.build_heap(array)
    # #  hp.build_heap(arr)
    #  hp.build_heap_max(array)
    # #  hp.build_heap_min(array)
    #  print("After heapify:")
    # #print(array)
    # #  print(array)
    # #  print(f"Extract or pop or delete_maximum: {hp.extract_max_or_pop(array)}")
    #  print(array)
     
    #  val = int(input("Insert element to heap: "))
    #  hp.insert_key_max_heap(array, val)
    #  print(array)
    #  print("Increasing key value:")
    #  hp.increase_key_max_heap(array, 11, 15)
    #  print(array)
    #  print("Decreasing key value:")
    #  hp.decrease_key_max_heap(array, 2, 9)
    #  print(array)
     print("Before sorting:",end=" ")
     print(array)
     hp.heapSort_max_heap(array)
     print()
     print("After sorting:",end="")
     print(array)