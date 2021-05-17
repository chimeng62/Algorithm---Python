# node class
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

# linkedList class
class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def read(self, index):
        currentNode = self.first_node
        currentIndex = 0
        # if search for index 0, it is first_node index
        if index == 0:
            return self.first_node.data
        while currentIndex < index:
            # keep following the links of each node
            # til reaching desired index
            currentNode = currentNode.next_node
            currentIndex += 1

            if currentIndex == index:
                return currentNode.data
        # if not found
        return None

    def findIndexOf(self, data):
        currentNode = self.first_node
        currentIndex = 0

        while currentNode:
            # base case when first_node data matches data searched for
            if currentNode.data == data:
                return currentIndex

            currentNode = currentNode.next_node
            currentIndex += 1
        # if not found
        return None

    def insertAtIndex(self,index,data):
        #create new node from data provided
        newNode = Node(data)
        #if insert at start
        if index == 0:
            #point newNode's nextNode to first_node
            newNode.next_node = self.first_node
            #set newNode as first_node node
            self.first_node = newNode
            return 
        #if insert anywhere else
        currentNode = self.first_node
        currentIndex = 0

        # index - 1 to locate the node just before the spot to be inserted
        while currentIndex < index - 1:
            currentNode = currentNode.next_node
            currentIndex +=1

        #set nextNode of our newNode's nextNode
        newNode.next_node = currentNode.next_node
        # Modify the link of the previous node to point to​ our new node:
        currentNode.next_node = newNode
        
    def deleteAtIndex(self,index):
        #if delete the first_node
        if index == 0:
            self.first_node = self.first_node.next_node
            return

        #if delete everywhere else
        currentNode = self.first_node
        currentIndex = 0
        #find node before the node to be deleted
        while currentIndex < index -1:
            currentNode = currentNode.next_node
            currentIndex +=1
        
        nodeAfterDeletedNode = currentNode.next_node.next_node
        currentNode.next_node = nodeAfterDeletedNode
    
    def printAllNode(self):
        ptr = self.first_node
        result = []
        while ptr:
            result.append(ptr.data)
            ptr = ptr.next_node
        return result

    def reverse(self):
        prevNode = None
        currentNode = self.first_node

        while currentNode:
            #shift all nodes 1 step back (None is the node before firstNode)
            nextNode = currentNode.next_node
            currentNode.next_node = prevNode
            prevNode = currentNode
            currentNode = nextNode
        
        self.first_node = prevNode