import sys
#Implementing min heap

class MinHeap:
    def __init__(self, heapSize):
        #create a complete binary tree using an array
        #then use the binary tree to construc a heap

        self.heapSize = heapSize

        #the number of elements is needed when instantiating an array
        #heapSize records the size of the array

        self.minheap = [0] * (heapSize + 1)

        #realSize records the number of elements in the heap
        
        self.realSize  = 0

        # function to add an element 

        def add(self, element):
            self.realSize += 1
            #if the number of elements in the heap exceeds the preset heapSize
            #print added too many elements and return
            if self.realSize > heapSize:
                print('added too many elements')
                self.realSize -= 1
                return

            #add the element into the array
            self.minheap[self.realSize] = element
            
            #index of the newly added element
            index = self.realSize
            #parent node of the newly added element
            #Note if we use an array to represent the complete binary tree
            #and store the root node at index 1
            #index of the parent node of any node is [index of the node / 2]
            #index of the left child node is [index of the node * 2]
            #index of the right child node is [index of the node * 2 + 1]
            parent = index // 2

            #if the newly added element is smaller than its parent node
            #its value will be exchanged with that of the parent node 

            while(self.minheap[index] < self.mindheap[parent] and index > 1):
                self.minheap[parent], self.minheap[index] = self.minheap[index], self.minheap[parent]

                index = parent
                parent = index // 2

            
    #get the top element of the heap
    def peek(self):
        return self.minheap[1]

    #delete the top element of the heap

    def pop(self):
        #if the number of element in the current Heap is 0,
        #print "don't have any element and return a default value"
        if self.realSize < 1:
            print("we don't have any elements!")
            return sys.maxsize
        else:
            #when there are still elements in the Heap
            #self.realSize >= 1
            removeElement = self.minheap[1]
            
            #put the last element of the Heap to the top of the heap
            self.minheap[1] = self.minheap[self.realSize]
            self.realSize -= 1
            index = 1

            #when the deleted element is not a leaf node
            while(index <= self.realSize // 2):
                #the left child of the deleted element
                left = index * 2
                
                #the right child of the deleted element
                right = (index * 2) + 1

                #if the deleted element is larger than the left or right child
                #its value needs to be exchanged with the smaller value
                #of the left and right child
                
                if(self.minheap[index] > self.minheap[left] or self.minheap[index] > self.minheap[right]):

                    if self.minheap[left] < self.meanheap[right]:
                        self.minheap[index], self.minheap[left] = self.minheap[left], self.meanheap[index]
                    else:
                        self.minheap[index], self.minheap[right] = self.minheap[right], self.minheap[index]
                        
                        index = right
                else:
                    break

        return removeElement


#return the number of elements in the heap

def size(self):
    return self.realSize

def _str_(self):
    return str(self.minheap[1 : self.realSize + 1])


if __name__ == "__main__":
    	# Test cases
        minHeap = MinHeap(5)
        minHeap.add(3)
        minHeap.add(1)
        minHeap.add(2)
        # [1,3,2]
        print(minHeap)
        # 1
        print(minHeap.peek())
        # 1
        print(minHeap.pop())
        # 2
        print(minHeap.pop())
        # 3
        print(minHeap.pop())
        minHeap.add(4)
        minHeap.add(5)
        # [4,5]
        print(minHeap)
            
            
        

       

        