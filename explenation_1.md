LRU Cache:

For Problem 1 (LRU Cache) I chose to use a doubly linked list and a dictionary. I chose these data strucutres because the doubly linked list. The doubly linked list stored the most recently used item and since a dictionary pointed to its nodes it had a constant run time of O(1). The space time complexity is O(n)

File Search:

For problem 2 I used recursion with an array list to store the elements I needed. Since I do not know how many subfolders a folder had I used iteration as well with a for loop bringing up the time complexity to O(log n). n is the number of groups and paths the function has to search through for runtime and each path could have either another path (directory) or the file that you want, so it is like searching through a tree.  The space complexity is O(n^2) due to the recursion. In this case n is the number of files in a directory * the number of subdirectories in a directory

Huffman Encoding:

For the third problem I used a heapq (priority queue) and a tree for huffman coding. The heapq had all the elements with the frequency so I coup pop the element with the lowest frequency in constant time. The tree was the structure allowing the code to be encoded and decoded. It had a runtime of O(log n) because of searching through the tree and a space complexity of O(n). The n in the runtime is for the encoded char getting sent through the tree. Since the char was actually what searched the tree the runtime becomes O(log n). The space n is for each, n, charecters in the original sentence.

User Search:

In problem 4 I used the given Group class which used an Arraylist data structure. I searched through this Arraylist which takes O(log n) time. Since each group could have a subgroup and each subgroup could have a user, it is similar to searching through a tree to find the leaf or in this case, user. The space complexity is O(n^2) which is the number of users in each group (n users) multiplied the number of groups and subgroups in the group (n total groups).

BlockChain:

For Problem 5 I used a linked list to orgainze the blocks. Each blockchain is effectively a linked list that cannot be changed. I used this data structure because all the blocks are connected and since you cannot change any element and only insert elements the time complexity is O(1) and the space complexity is O(n)

Linked List Manipulation:

For Problem 6 I was given linked list and I had to compare them. I searched through the linked lists to find a value and I used a dictionary to store the values. I chose a dictionary because it has constant lookup, insertion, and deletion time. The elements were then put back into a linked list, and all the processes besides searching the linked list were O(1), making the runtime O(n) and the space complexity O(n)


