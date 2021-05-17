#import classes from node.py
from linkedList import *

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
e.next_node = f

myList = LinkedList(a)

#print(myList.findIndexOf("A"))
#print(myList.read(2))

#myList.insertAtIndex(2,"CHIMENG")
print(myList.printAllNode())

#myList.deleteAtIndex(2)
myList.reverse()
#print linkedList
print(myList.printAllNode())
