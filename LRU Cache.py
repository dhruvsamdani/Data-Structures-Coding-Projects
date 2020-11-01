

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables

        self.capacity = capacity
        self.dict = {}
        self.LinkedList = LinkedList()

        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        if key in self.dict:
            value = self.dict[key]
            if value.prev == None:
                self.LinkedList.tail.next = value
                self.LinkedList.head = value.next
                self.LinkedList.head.prev = None
                value.next = None
                value.prev = self.LinkedList.tail
                self.LinkedList.tail = value
            else:
                value.prev.next = value.next
                value.next = self.LinkedList.head
                self.LinkedList.head = value
                value.prev = None
                
            return print(value.value)
        return print(-1)

        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacity == None:
            print('Invalid capacity')
            return
        if len(self.dict) == self.capacity:
            head = self.LinkedList.head
            self.LinkedList.tail.next = Node(value)
            self.LinkedList.tail.next.prev = self.LinkedList.tail
            self.LinkedList.tail  = self.LinkedList.tail.next
            self.LinkedList.head = head.next
            self.LinkedList.tail.key = key
            self.dict[key] = self.LinkedList.tail #OFF
            # self.LinkedList.head.next = head.next
            head.prev = None
            head.next = None
            
            self.LinkedList.head.prev = None
            self.dict.pop(head.key)

            return -1
        if self.LinkedList.head == None:
            self.LinkedList.head = Node(value)
            self.dict[key] = self.LinkedList.head
            self.LinkedList.head.key = key
            self.LinkedList.tail = self.LinkedList.head

        else:

            self.LinkedList.tail.next = Node(None)
            self.LinkedList.tail.next.prev = self.LinkedList.tail
            self.LinkedList.tail = self.LinkedList.tail.next
            self.LinkedList.tail.value = value
            self.dict[key] = self.LinkedList.tail
            self.LinkedList.tail.key = key
            



class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.key = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.set(7, 7)
our_cache.get(4)

print('----------------------------testCase1---------------------------')
testCase2 = LRU_Cache(6)

testCase2.set(None,None)
testCase2.set(1,3)
testCase2.set(4,5)
testCase2.set(2,3)

testCase2.get(None) # returns None
testCase2.get(4)    # returns 5
testCase2.get(28)   # returns -1

testCase2.set(15,3)
testCase2.set(4,7)
testCase2.set(5,38)
testCase2.set(8,9)

testCase2.get(4) # return -1


print('----------------------------testCase2---------------------------')
testCase3 = LRU_Cache(None) 
testCase3.set(15,3) # Invalid capacity

testCase3.get(7) # -1

testCase3.set(16,7) # Invalid capacity

testCase3.get(15)   # -1

testCase3.get(16)   # -1

print('----------------------------testCase3---------------------------')
cache = LRU_Cache( 2)

cache.set(1, 1)
cache.set(2, 2)
cache.get(1)   # 1  
cache.set(3, 3);   
cache.get(2)   # -1 
cache.set(4, 4)    
cache.get(1)   # -1    
cache.get(3)   # 3    
cache.get(4)   # 4    
