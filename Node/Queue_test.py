#import classes from node.py
from Queue import *

#a = Node("A")
# b = Node("B")
# c = Node("C")
# d = Node("D")
# e = Node("E")
# f = Node("F")

# a.next_node = b

# b.prev_node = a
# b.next_node = c

# c.prev_node = b
# c.next_node = d

# d.prev_node = c
# d.next_node = e

# e.prev_node = d
# e.next_node = f

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
print(q.getSize())

print(q.printQueue())
q.dequeue()
print(q.getSize())
print(q.printQueue())
q.dequeue()
print(q.getSize())
print(q.printQueue())
print(q.isEmpty())
