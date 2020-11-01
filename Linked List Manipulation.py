class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    returnList = LinkedList()
    valueDict = {}
    ll1_head = llist_1.head
    ll2_head = llist_2.head
    while llist_1.head:
        # returnList.append(llist_1.head.value)
        valueDict[llist_1.head.value] = ''
        llist_1.head = llist_1.head.next

    while llist_2.head:
        if llist_2.head.value in valueDict:
            llist_2.head = llist_2.head.next
        else:
            # returnList.append(llist_2.head.value)
            valueDict[llist_2.head.value] = ''
            llist_2.head = llist_2.head.next

    for item in valueDict:
        returnList.append(item)

    llist_1.head = ll1_head
    llist_2.head = ll2_head
    return returnList
    pass

def intersection(llist_1, llist_2):
    # Your Solution Here
    returnList = LinkedList()
    valueDict = {}
    while llist_1.head:
        valueDict[llist_1.head.value] = llist_1.head.value
        llist_1.head = llist_1.head.next

    while llist_2.head:
        if llist_2.head.value in valueDict:
            returnList.append(valueDict.pop(llist_2.head.value))

        llist_2.head = llist_2.head.next
    return returnList



# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ('U: ',union(linked_list_1,linked_list_2)) # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
print ('I: ',intersection(linked_list_1,linked_list_2)) # 6 -> 4 -> 21 -> 

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ('U2: ',union(linked_list_3,linked_list_4)) # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
print ('I2: ',intersection(linked_list_3,linked_list_4)) # 

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,1,1,1,1,1,1,1]
element_2 = [1,1,1,1,1,1,1,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print ('U3: ',union(linked_list_5,linked_list_6)) # 1 ->
print ('I3: ',intersection(linked_list_5,linked_list_6)) # 1 ->

# Test case 4

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [(4,5),(5,6)]
element_2 = [(5,6),None]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print ('U4: ',union(linked_list_7,linked_list_8)) # (4, 5) -> (5, 6) -> None -> 
print ('I4: ',intersection(linked_list_7,linked_list_8)) # (5, 6) -> 


