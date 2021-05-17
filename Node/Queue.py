# node class
class Node:
    def __init__(self, data=None,prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node
        
# linkedList class
class Queue:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.size = 0
    #insertAtEnd
    #Doubly Linked List used here to add to append node after last_node 
    def enqueue(self,data):
        #create new node from data provided
        newNode = Node(data)

        if self.first_node == None:
            self.first_node = newNode
            self.last_node = newNode
        else:
            newNode.prev_node = self.last_node
            self.last_node.next_node = newNode
            self.last_node = newNode
        self.size +=1

    #remove from front
    def dequeue(self):
            removedNode = self.first_node
            self.first_node = self.first_node.next_node
            self.size -=1
            return removedNode

    #return first node
    def getFirst(self):
        return self.first_node.data

    #return queue size
    def getSize(self):
        return self.size
    
    #return true if queue is empty
    def isEmpty(self):
        if self.first_node is None:
            return True
        return False

    def printQueue(self):
        ptr = self.first_node
        result = ""
        while ptr:
            result+=(ptr.data)
            result+=" -> "
            ptr = ptr.next_node
        return result
    
    




